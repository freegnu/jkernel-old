from ctypes import *

import sys

def get_libj(path):
    libj = cdll.LoadLibrary(path)

    libj.JInit.restype = c_void_p
    libj.JSM.argtypes = [c_void_p, c_void_p]
    libj.JDo.argtypes = [c_void_p, c_char_p]
    libj.JDo.restype = c_int
    libj.JFree.restype = c_int
    libj.JFree.argtypes = [c_void_p]

    return libj

class JWrapper:
    def __init__(self):

        binpath = "/home/adrian/j64-804/bin"

        self.libj = get_libj(binpath + "/libj.so")
        self.j = self.libj.JInit()

        OUTPUT_CALLBACK = CFUNCTYPE(None, c_void_p, c_int, c_char_p)
        INPUT_CALLBACK = CFUNCTYPE(c_char_p, c_void_p, c_char_p)

        def output_callback(j, output_type, result):
            output_types = [None, "output", "error", "output log", "assert", "EXIT", "1!:2[2 (wat)"]
            self.output_type = output_types[output_type]
            self.output = result.decode('utf-8', 'replace')

        def input_callback(j, prompt):
            return b")"

        callbacks_t = c_void_p*5
        callbacks = callbacks_t(
            cast(OUTPUT_CALLBACK(output_callback), c_void_p),
            0,
            cast(INPUT_CALLBACK(input_callback), c_void_p),
            0,
            c_void_p(3) # defines "console" front-end (see jconsole.c, line 128)
        )
        self.libj.JSM(self.j, callbacks)

        self.sendline("ARGV_z_=:''")
        self.sendline("BINPATH_z_=:'{}'".format(binpath))
        self.sendline("1!:44'{}'".format(binpath))
        self.sendline("0!:0 <'profile.ijs'")

    def close(self):
        self.libj.JFree(self.j)

    def sendline(self, line):
        self.output = None
        self.libj.JDo(self.j, c_char_p(line.encode()))
        if not self.output:
            return ""
        return self.output

if __name__ == "__main__":
    j = JWrapper()
    j.sendline("load 'viewmat'")
    j.sendline("load 'bmp'")
    j.sendline("VISIBLE_jviewmat_ =: 0")
    #j.sendline("viewmat i. 5 5")
    j.close()
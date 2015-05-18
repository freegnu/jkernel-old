from IPython.kernel.zmq.kernelbase import Kernel
import pexpect

class JKernel(Kernel):
    implementation = 'jkernel'
    implementation_version = '0.1'
    language_info = {
        'mimetype': 'text/plain',
        'name': 'J',
        'file_extension': 'ijs'
    }
    banner = "J language kernel"
    help_links = [
        {'text': 'Vocabulary', 'url': 'http://www.jsoftware.com/help/dictionary/vocabul.htm'},
        {'text': 'NuVoc', 'url': 'http://www.jsoftware.com/jwiki/NuVoc'}
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.j = pexpect.spawn("/home/adrian/j803/bin/jconsole")

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):

        lines = code.splitlines()

        for line in lines:
            self.j.sendline(line)

        separator = "jkernel_separator=:0"
        self.j.sendline(separator)
        self.j.expect("\r\n   " + separator + "\r\n   ")

        if not silent:
            output = self.j.before.decode().strip("\n").splitlines()[len(lines):]
            output = "\n".join(output)
            stream_content = {'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

    def do_inspect(self, code, cursor_pos, detail_level=0):

        inspection = "u@v  mv lv rv \nAtop \n\nx u@v y ↔ u x v y\n4523545"

        return {
            'status': 'ok',
            'data': {'text/plain': inspection},
            'metadata': {},
            'found': True
        }


if __name__ == '__main__':
    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=JKernel)
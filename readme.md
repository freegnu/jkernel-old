![](http://i.imgur.com/wL5ZTfu.png)

To install: place the files in ~/.ipython/kernels/jkernel directory. Make sure that the path to jconsole in the script is okay. Open `ipython notebook` from this directory.

Install pexpect module for Python.

Requires IPython 3.0+.

(jkernel.py should be placed in Python's `dist-packages` directory to be accessible from everywhere, but that's not important at this stage)

Won't currently work on Windows because of pexpect.

Not sure if will work in Python2, tested on Py3 only.

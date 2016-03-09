![](http://i.imgur.com/wL5ZTfu.png)

To install: place the files in ~/.ipython/kernels/jkernel* directory. Rename "config-sample.ini" to "config.ini" and change the paths to match your setup. Open `jupyter notebook` (or `ipython notebook`, but it's deprecated) from this directory.

(* or the newer location: `~/.local/share/jupyter/kernels/jkernel` on Linux, `%APPDATA%\jupyter\kernels\jkernel` on Windows, `~/Library/Jupyter/kernels/jkernel` on OSX.)

Requires IPython 3.0+, possibly 4.0+.

(in theory jkernel.py should be placed in Python's `dist-packages` directory to be accessible from everywhere, but that's not important at this stage)

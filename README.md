py-mmap (still a work in progress)
=======
py-mmap is an abstraction layer built on top of Python's built-in mmap module. In many ways, this project is inspired by the mmap-go package. which can be found [here](https://github.com/edsrzf/mmap-go)

Overview
=======
Just like its predecessor, py-mmap allows mapping files into memory. 
Providing a simple and portable interface, py-mmap doesn't go out of its way to abstract away every little platform detail.

Developer Notes
=======
For more information about its internal implementation, please take a look at [utils.py](https://github.com/thaibui2308/py-mmap/blob/main/utils.py) and [py-mmap.py](https://github.com/thaibui2308/py-mmap/blob/main/utils.py) and also keep in mind that this module is a Python version of the mmap-go package.
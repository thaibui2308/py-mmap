import mmap


F_RDONLY = 0
F_RDWR = 1 
F_COPY = 4
F_EXEC = 8

F_ANON = 1

ACCESS_MAPPING = {
    F_RDONLY: mmap.ACCESS_READ,
    F_RDWR: mmap.ACCESS_DEFAULT,
    F_COPY: mmap.ACCESS_COPY,
    F_ANON: mmap.ACCESS_DEFAULT
}

INTERCHANGING_FLAGS = {
    F_RDONLY: 'r',
    F_RDWR: 'r+',
    F_COPY: 'r',
    F_ANON: 'r+'
}
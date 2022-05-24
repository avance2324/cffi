from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef("int addme(int a, int b);")
ffibuilder.set_source("pyadd",'#include "add.h"',sources=["add.c"])
if __name__ == "__main__":
    ffibuilder.compile()

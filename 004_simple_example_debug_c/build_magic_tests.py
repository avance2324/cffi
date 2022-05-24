from cffi import FFI

ffibuilder = FFI()

# For every function that you want to have a python binding,
# specify its declaration here
ffibuilder.cdef("""
    int add(int a, int b);
                """)

# Here go the sources, most likely only includes and additional functions if necessary
ffibuilder.set_source("magic_tests",
    """
    #include "magic.h"
    """, sources=["magic.c"])

if __name__ == "__main__":
    ffibuilder.compile()
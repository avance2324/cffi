import os
from cffi import FFI

## provide C file header and source
header="../c/magic.h"
source="../c/magic.c"

## ==========================================================

ffibuilder = FFI()

# For every function that you want to have a python binding,
# specify its declaration here
ffibuilder.cdef("""
    int add(int a, int b);
                """)
                
# Here get the sources, most likely only includes and additional functions if necessary
ffibuilder.set_source("_magic",
    f"""
    #include "{header}"
    """, sources=[ source ])

if __name__ == "__main__":
    ffibuilder.compile()


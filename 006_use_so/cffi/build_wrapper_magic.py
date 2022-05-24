import os
from cffi import FFI

header="magic.h"
##shared_lib="../c/build/magic.c"

## ==========================================================
# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder = FFI()


# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
    int add(int a, int b);
                """)
                

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string. This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
# 
#  1.  first argumernt is name of generated python module, here is "_magic"
#  2.  second argument 
ffibuilder.set_source("_magic",
    f"""
        #include "{header}" // the C header of the library 
    """,
    include_dirs = ['../c/include/'], ## path of header file, magic.h
    library_dirs = ['../c/build/'],   ## path of shared library generated from c code
    libraries=[ 'magic' ],)           ## name of shared library, here it is libmagic.so
##ffibuilder.set_source("_magic",
##    f"""
##    #include "{header}"
##    """, sources=[ source ])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)


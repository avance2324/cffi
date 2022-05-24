Overview
=======================================================
 This example shows how to create cffi wrapper based on 
 shard library
 
 
 

Structure
=========================================================
<this dir>
  |
  |-- c/      # c source code: .c, .h
  |    |
  |    |-- src/
  |    |     |
  |    |     +-- do_print.c
  |    |     |
  |    |     +-- magic.c
  |    |
  |    +-- include/
  |          |
  |          |-- do_print.h
  |          |
  |          +-- magic.h
  |
  |-- python/ # python file to test 
  |    |
  |    +-- test_magic.py
  |
  +-- cffi/
       |
       +-- build_wrapper_magic.py  


how to run
=========================================================
1.  . build.scr
        - build shared library c/build/libmagic.so based on code
        - build cffi wrapper cffi/_magic.**.so based on libmagic.so 
2.  . run.scr
        run python/test_magic.py to test cffi wrapper.


how to debug
=========================================================
1.  how to debug c code 
    code .
    in terminal, type . build.scr
    open magic.c 
    set breakpoint
    press F5 to debug

2.  how to debug python code 
    cd python
    code .
    in terminal, type . build.scr
    open test_magic.py
    set break point
    in vscode terminal, type . set_path.scr    
    press F5 to debug


  



question/notes
=========================================================
1.  how to tell cffi to build wrapper based on shared library?
    <= see cffi/build_wrapper_magic.py
          ffibuilder.set_source("_magic",
          f"""
              #include "{header}"
          """,
          include_dirs = ['../c/include/'],
          library_dirs = ['../c/build/'],
          libraries=[ 'magic' ],)

2.  which environment variable should be set in order to run cffi wrapper ?
    <= see set_path.scr  
        export PYTHONPATH = ./cffi
        export PYTHONPATH = ./c/build 
        export LD_LIBRARY_PATH = ./c/build  ## because libmagic.so is here!

3.  why I need to set up LD_LIBRARY_PATH ?
    <= because the cffi wrapper is built from libmagic.so, 
       in the generate wrapper _magic.**.so, it doesn't tell where is 
       the c source code and header (use strings to check)
       Therefore we need to tell the python the location of libmagic.so 
       via LD_LIBRARY_PATH

4.  if function magic() call sub function do_print(), do I need to 
    add do_print() to ffibuilder.cdef() of build_wrapper_magic.py?
    <= now, you only need to add the function that you want to call, which 
        is add, like this:
        ffibuilder.cdef("""
                       int add(int a, int b);
                    """)

5.  If I have global variables in my c program, do I need to add then 
    in build script for cffi?
    <= no
       see these global variables defined in magic.h
          int glob_var_10 = 10 ;
          int glob_var_20 = 20 ;
       they are used by magic.c, but you don't need to specify them

6.  if I change the C code, what should I do 
    <= If following parts are not changed, we only need to cmake && make the 
       share library from C, we don't need to rebuild cffi.
        (1)  interface of function add() is not change, 
        (2)  the header file that declare add() is not changed.
        (3)  the includ dir is not changed
        (4)  the library_dir is not changed
        (5)  the name of shared library is not changed.


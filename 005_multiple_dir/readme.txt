Overview
=======================================================
 This example shows how to build and wrapper from source
 which is not in current directory


 

Structure
=========================================================
<this dir>
  |
  |-- c/      # c source code: .c, .h
  |    |
  |    |-- magic.c
  |    |
  |    +-- magic.h
  |
  |-- python/ # python file to test 
  |    |
  |    +-- test_magic.py
  |
  |-- cffi/
       |
       +-- build_wrapper_magic.py  


how to run
=========================================================
1.  . set_path.scr # setup the PYTHONPATH
2.  . build.scr
3.  . run.scr

Overview
================================================
test the use of cffi to wrappar c for python test bench
debug the python code 
debug the c code



Principle
================================================
1) define a build_**.py to build a .so file which can be 
   imported by python

2) in python, import the module from the *.so


Examples
================================================
001_simple_example
-------------------------------
   A simple example, it works fine


002_simple_example
   Another simple example, it works fine
     


003_simple_example_debug_python
-------------------------------
   debug python code
   1. clean up
      . clear.scr
   2. build
      . build.scr
   3. in vscode set breakpoint in python_build_magic_test.py
   4. press F5 to debug


004_simple_example_debug_c
-------------------------------
   debug c code
   1. create .vscode/launch.json based on C++(GDB/LLDB)
   2. add following line to launch.json 
         "program": "/home/fjxvn4/Python3/Python-3.7.6/bin/python3",
         "args": ["${workspaceFolder}/python_build_magic_tests.py"],
   3. in terminal
      . clean.scr
      . build.scr
   4. in vscode, set break point in magic.c 
   5. press F5 to debug


question/notes
================================================

cmake_minimum_required(VERSION 3.10.2)
project(magic)

## store all header files in include/
## the path used by include_directories is relative to
## the path where CMakeLists.txt is located.
include_directories(./include)

## can manually add the source files using set command
# set(SOURCES src/mainapp.cpp src/student.cpp)

## however, the file(GLOB...) allows for wildcard additions
##file(GLOB SOURCES "../../src/*.c")
set(SOURCES 
./src/magic.c
./src/do_print.c
)

###add_executable(student ${SOURCES})
add_library(magic SHARED ${SOURCES})
set(CMAKE_BUILD_TYPE Debug)

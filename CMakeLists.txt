cmake_minimum_required(VERSION 3.8)
project(openarinc)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB_RECURSE headers openarinc/src/*.hpp)
file(GLOB_RECURSE sources openarinc/src/*.cpp)
add_library(${PROJECT_NAME} STATIC ${headers} ${sources})
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/openarinc/src)

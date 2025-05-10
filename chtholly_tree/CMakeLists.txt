
cmake_minimum_required(VERSION 3.10)

project(ChthollyTree 
        LANGUAGES CXX)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/bin)
set(EXECUTABLE_NAME chtholly_tree)

file(GLOB SOURCE_FILES
    ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

set(VCPKG_ROOT "D:/vcpkg/vcpkg")  

set(GTEST_INCLUDE_DIR "${VCPKG_ROOT}/installed/x64-windows/include")  
set(GTEST_LIBRARY "${VCPKG_ROOT}/installed/x64-windows/lib/gtest.lib") 

include_directories(${GTEST_INCLUDE_DIR})  

add_executable(${EXECUTABLE_NAME} ${SOURCE_FILES})

target_link_libraries(${EXECUTABLE_NAME} ${GTEST_LIBRARY})  

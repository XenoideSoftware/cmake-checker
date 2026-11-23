cmake_minimum_required (VERSION 3.25)
project (cmake-checker LANGUAGES CXX)

include(XenoideConfig)

set(XE_ENABLE_TESTING "${XENOIDE_ENABLE_TESTING}" CACHE BOOL "Enable the unit test suite" FORCE)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

find_package(cxxopts CONFIG REQUIRED)

add_subdirectory("src")

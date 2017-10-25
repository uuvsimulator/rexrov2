cmake_minimum_required(VERSION 2.8.3)
project(rexrov2_description)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY meshes robots urdf launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
        PATTERN "*~" EXCLUDE)

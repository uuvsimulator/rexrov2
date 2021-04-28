cmake_minimum_required(VERSION 3.5)
project(rexrov2_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch xacro meshes robots
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

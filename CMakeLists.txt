cmake_minimum_required(VERSION 3.8)
project(hesai_description)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(xacro REQUIRED)


# Install directories
install(DIRECTORY config launch urdf
  DESTINATION share/${PROJECT_NAME}
)

# Process and install xacro files
foreach(xacro_file ${xacro_files})
  get_filename_component(filename ${xacro_file} NAME)
  xacro_add_xacro_file(${xacro_file} ${filename})
  install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${filename}
    DESTINATION share/${PROJECT_NAME}/urdf
  )
endforeach()

ament_package()

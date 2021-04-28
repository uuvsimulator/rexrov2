import os

import launch
import launch_ros.actions
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

import xacro


def generate_launch_description():
    
    x = LaunchConfiguration('x', default='0.0')
    y = LaunchConfiguration('y', default='0.0')
    z = LaunchConfiguration('z', default='1.0')
    pkg_share = FindPackageShare('rexrov2_description').find('rexrov2_description')
    robots_dir = os.path.join(pkg_share, 'robots')
    xacro_file = os.path.join(robots_dir, 'rexrov2_default.xacro')
    doc = xacro.process_file(xacro_file)
    robot_desc = doc.toprettyxml(indent='  ')
    params = {'robot_description': robot_desc}

    gazebo = ExecuteProcess(
          cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
          output='screen')

    rsp = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[params])

    spawn_entity = Node(
            package='gazebo_ros', 
            executable='spawn_entity.py',
            arguments=['-entity', 'rexrov2', '-topic', '/robot_description',
                    '-x',  x, '-y', y, '-z', z],
            output='screen')
            
    return LaunchDescription([
        gazebo,
        rsp,
        spawn_entity,
    ])

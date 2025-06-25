from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():
    # Launch arguments
    simulation_arg = DeclareLaunchArgument(
        'simulation',
        default_value='false',
        description='Simulation mode'
    )
    
    # Get the URDF via xacro
    robot_description_content = Command(
        [
            FindExecutable(name='xacro'), ' ',
            PathJoinSubstitution([FindPackageShare('hesai_description'), 'urdf', 'hesai_standalone.urdf.xacro']),
            ' ', 'simulation:=', LaunchConfiguration('simulation')
        ]
    )
    
    robot_description = {'robot_description': robot_description_content}

    return LaunchDescription([
        simulation_arg,
        # Publish robot description
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[robot_description]
        )
    ])

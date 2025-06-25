from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():
    # Launch arguments
    rviz_arg = DeclareLaunchArgument(
        'rviz',
        default_value='true',
        description='Start RViz'
    )
    
    simulation_arg = DeclareLaunchArgument(
        'simulation',
        default_value='true',
        description='Simulation mode'
    )
    
    # Include the load.launch file
    load_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('hesai_description'),
                'launch',
                'load.py'
            ])
        ]),
        launch_arguments={
            'simulation': LaunchConfiguration('simulation')
        }.items()
    )
    
    # RViz node
    rviz_config_file = PathJoinSubstitution([
        FindPackageShare('hesai_description'),
        'config',
        'rviz',
        'display_urdf.rviz'
    ])
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz',
        arguments=['-d', rviz_config_file],
        condition=IfCondition(LaunchConfiguration('rviz'))
    )
    
    return LaunchDescription([
        rviz_arg,
        simulation_arg,
        load_launch,
        rviz_node
    ])


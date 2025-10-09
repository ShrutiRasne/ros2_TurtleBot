from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_bringup',
            executable='bringup_launch',
            output='screen',
            parameters=[{'use_sim_time': True, 'map': '/home/shruti/ros2_turtlebot3_project/maps/quadruped_map.yaml'}]
        )
    ])

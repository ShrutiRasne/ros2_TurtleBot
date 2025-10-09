from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/home/shruti/ros2_turtlebot3_project/src/turtlebot3_nav2/launch/nav2_default_view.rviz']
        )
    ])

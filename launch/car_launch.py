from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='python_parameters',
            #namespace='listener',
            executable='listener',
            name='listener'
        ),
        Node(
            package='python_parameters',
            #namespace='talker',
            executable='talker',
            name='talker'
        )
    ])

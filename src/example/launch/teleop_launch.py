import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():

    # Check if we're told to use sim time
    #use_sim_time = LaunchConfiguration('use_sim_time')
    
    #print(os.getcwd())
    #if(not os.path.isdir(os.path.join(os.getcwd(),'maps'))):
    #    os.mkdir('maps')

    pkg_path = os.path.join(get_package_share_directory('example'))
 
    teleop_params = os.path.join(pkg_path,'config','teleop_keyboard.yaml')

    print("AAA", teleop_params)
    
    # Create a map_saver node
    
    node_teleop = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        parameters=[teleop_params,]
    )


    # Launch!
    return LaunchDescription([
        #DeclareLaunchArgument(
            #'use_sim_time',
            #default_value='false',
            #description='Use sim time if true'),
        node_teleop
    ])
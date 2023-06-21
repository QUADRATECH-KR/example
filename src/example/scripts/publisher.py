#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class PUB_Node(Node):
        duration = 0.2

        def timer_callback(self):
              twist_ = Twist()
              twist_.linear.x = random.random()
              twist_.angular.z = random.random()
              
              self.pub.publish(twist_)
              print("Published Data")

        def __init__(self):
                super().__init__("pub_node")   #Node Name
                self.pub  =  self.create_publisher(Twist, 'cmd_vel', 2)

                self.timer_ = self.create_timer(self.duration, self.timer_callback)



def main(args = None):
      rclpy.init(args = args)
      node_ = PUB_Node()
      try:
             rclpy.spin(node_)
      except KeyboardInterrupt:
             pass
      node_.destroy_node()
      rclpy.shutdown()
if __name__ == '__main__':
      main()

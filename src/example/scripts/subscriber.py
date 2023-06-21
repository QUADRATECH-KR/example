#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SUB_Node(Node):
        def sub_callback(self, msg):
              print("linear    x : ", msg.linear.x)
              print("angular   z : ", msg.angular.z)
        def __init__(self):
                super().__init__("sub_node")   #Node Name
                self.sub  =  self.create_subscription(Twist, 'cmd_vel', self.sub_callback, 2)



def main(args = None):
      rclpy.init(args = args)
      node_ = SUB_Node()
      try:
             rclpy.spin(node_)
      except KeyboardInterrupt:
             pass
      node_.destroy_node()
      rclpy.shutdown()
if __name__ == '__main__':
      main()

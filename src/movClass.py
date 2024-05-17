#Este codigo foi feito baseado no projeto do grupo 4 + a ponderada de turtlesim (https://github.com/GalloGGMC/PonderadaTurtlesim1)

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class Movimento(Node):
    def __init__(self,vx,vy,vt,t):
        super().__init__("movimento")
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel",10)
        self.vx = vx
        self.vy = vy
        self.vt = vt
        self.t = t
        self.finished = False

    def exec(self):
        return self.finished
    
    def start(self):
        msg = Twist()
        msg.linear.x, msg.linear.y, msg.angular.z = self.vx,self.vy,self.vt
        self.publisher_.publish(msg)
        now = time.time()
        while time.time() - now >= self.t:
            pass
        msg.linear.x, msg.linear.y, msg.angular.z = 0.0,0.0,0.0
        self.finished = True

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Movimento(1.0,0.0,1.57,2.0)

    rclpy.spin(minimal_publisher)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
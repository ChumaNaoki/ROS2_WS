import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):     #Nodeというクラスの機能を受け継いだクラスになる
    def __init__(self):            #オブジェクトができたときに呼ばれ
        super().__init__("takler") #Nodeのオブジェクトとしての初期化
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(0.5, self.cb)
        self.n = 0


def cd(self):
    msg = Int16()
    msg.data = self.n
    self.pub.publish(msg)
    self.n += 1


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)

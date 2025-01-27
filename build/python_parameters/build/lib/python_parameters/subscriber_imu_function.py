import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
import serial
import time

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('imu_subscriber')
        self.subscription = self.create_subscription(Float32MultiArray, 'imu_euler', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        arduino_port = '/dev/ttyACM0'
        baud_rate = 115200  # Match this with the baud rate set in your Arduino code
        self.arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
        time.sleep(2)

    def listener_callback(self, msg):
        message = "imuAngle:"+str(msg.data[0])+"\n"
        self.get_logger().info('I heard: "%s"' % message)
        # self.send_data_serial(message)
    
    def send_data_serial(self, message):
        try:
            self.arduino.write(message.encode())  # Encode the string into bytes
            # print("imuAngle:"+str(message[0]))

        except serial.SerialException as e:
            print(f"Error: {e}")

        # finally:
        #     if 'arduino' in locals() and self.arduino.is_open:
        #        self.arduino.close()
        #        print("Connection closed.")

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Float32MultiArray
import serial
import time

import re

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String, 'car', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        self.imu_subscription = self.create_subscription(Float32MultiArray, 'imu_euler', self.imu_listener_callback, 10)
        self.imu_subscription  # prevent unused variable warning
        arduino_port = '/dev/ttyACM0'
        baud_rate = 115200  # Match this with the baud rate set in your Arduino code
        self.arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
        self.angle = -1
        time.sleep(2)

    def listener_callback(self, msg):
        command_message = msg.data
        self.get_logger().info('I heard: "%s"' % command_message)
        self.send_data_serial(command_message)

        match = re.search(r'angle:([-]?\d+)', command_message)
        if match:
            self.angle = int(match.group(1))
    
    def imu_listener_callback(self, msg):
        imu_message = msg.data[0]
        if imu_message <= 360:
            self.get_logger().info('I heard: "%s"' % imu_message)
            if self.angle != -1:
                self.corr_direction(imu_message)
    
    def send_data_serial(self, message):
        try:
            self.arduino.write(message.encode())  # Encode the string into bytes
            print(f"Sent: {message}")

        except serial.SerialException as e:
            print(f"Error: {e}")

#        finally:
#            if 'arduino' in locals() and self.arduino.is_open:
#                self.arduino.close()
#                print("Connection closed.")

    def corr_direction(self, imu):
        real_angle = imu
        if 30 >= real_angle - self.angle >=1 or -330 >= real_angle - self.angle >= -359:
            self.get_logger().info('turn left')
            self.arduino.write("direction:-0.1\n".encode())  # turn to left at 1 degree
        elif 30 >= self.angle - real_angle >=1 or -330 >= self.angle - real_angle >= -359:
            self.arduino.write("direction:0.1\n".encode())  # turn to right at 1 degree
            self.get_logger().info('turn right')

        return 1

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

source ./install/setup.bash

ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.5 distance:8.17 angle:0 direction:0}"
sleep 16.34
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.3 distance:5 angle:-1 direction:-0.336}"
sleep 16.67
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.5 distance:2.85 angle:188 direction:0}"
sleep 5.7
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.3 distance:2.2 angle:-1 direction:-0.35}"
sleep 7.34
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.3 distance:0.5 angle:115 direction:0}"
sleep 1.67
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.3 distance:2 angle:-1 direction:0.6}"
sleep 6.67
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.3 distance:0.8 angle:225 direction:0}"
sleep 2.67
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.3 distance:1.5 angle:-1 direction:-0.46}"
sleep 5
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.3 distance:0.4 angle:150 direction:0}"
sleep 1.34
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.3 distance:1.8 angle:-1 direction:-0.37}"
sleep 6
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.3 distance:1.8 angle:-1 direction:-0.5}"
sleep 6
ros2 topic pub -1 /car std_msgs/msg/String "{data: speed:0.3 distance:0.01 angle:-1 direction:0}"

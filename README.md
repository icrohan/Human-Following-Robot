# Human-Following-Robot
Human-following robot using OpenCV and an ESP32 involves a combination of computer vision, microcontroller programming, and hardware interfacing.

*Components Needed*
ESP32
Camera module (e.g., ESP32-CAM)
Motor driver (e.g., L298N)
DC motors and wheels
Chassis for the robot
Power supply
Computer for running OpenCV

*High-Level Overview*
Use OpenCV to detect and track a human: Capture frames from a camera, process them to detect a human, and determine the position of the human in the frame.
Send control commands to the ESP32: Based on the position of the human, send control signals to the ESP32 to move the robot.
Control the robot's movement: Use the ESP32 to drive the motors and make the robot follow the human.

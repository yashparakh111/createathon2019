from gpiozero import DistanceSensor
import time

LEFT_ECHO_PIN = 14
LEFT_TRIG_PIN = 15

MOTION_ECHO_PIN = 24
MOTION_TRIG_PIN = 10

RIGHT_ECHO_PIN = 19
RIGHT_TRIG_PIN = 26

DEPTH_ECHO_PIN = 9
DEPTH_TRIG_PIN = 11

MOTION_THRESHOLD_DIST = 0.3

left_sensor_ultrasonic = DistanceSensor(echo = LEFT_ECHO_PIN, trigger = LEFT_TRIG_PIN, threshold_distance = THRESHOLD_DIST)
motion_sensor_ultrasonic = DistanceSensor(echo = MOTION_ECHO_PIN, trigger = MOTION_TRIG_PIN, threshold_distance = MOTION_THRESHOLD_DIST)
right_sensor_ultrasonic = DistanceSensor(echo = RIGHT_ECHO_PIN, trigger = RIGHT_TRIG_PIN, threshold_distance = THRESHOLD_DIST)

motion_sensor_ultrasonic.wait_for_in_range()
print("LEFT SENSOR TRIGGERED!")


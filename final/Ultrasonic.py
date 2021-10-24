# uses ultrasonic sensor within the receptacle
# to look for a different distance
from gpiozero import DistanceSensor

ERROR_THRESHOLD = 0.1
EMPTY_RECEPTACLE_DIST = 0.3

LEFT_ECHO_PIN = 14
LEFT_TRIG_PIN = 15

RIGHT_ECHO_PIN = 19
RIGHT_TRIG_PIN = 26

DEPTH_ECHO_PIN = 9
DEPTH_TRIG_PIN = 11

MOTION_ECHO_PIN = 24
MOTION_TRIG_PIN = 10

#left_sensor_ultrasonic = DistanceSensor(echo = LEFT_ECHO_PIN, trigger = LEFT_TRIG_PIN, max_distance = 2)
#right_sensor_ultrasonic = DistanceSensor(echo = RIGHT_ECHO_PIN, trigger = RIGHT_TRIG_PIN, max_distance = 2)
#motion_sensor_ultrasonic = DistanceSensor(echo = MOTION_ECHO_PIN, trigger = MOTION_TRIG_PIN, max_distance = 2)
#depth_sensor_ultrasonic = DistanceSensor(echo = DEPTH_ECHO_PIN, trigger = DEPTH_TRIG_PIN, max_distance = 2)

def isMotionDetected():
    if abs(motion_sensor_ultrasonic.distance - EMPTY_RECEPTACLE_DIST) > ERROR_THRESHOLD:
        return True
    return False


def getDistRight(): 
    return right_sensor_ultrasonic.distance

def getDistLeft():
    return left_sensor_ultrasonic.distance

def getBinDepth():
    return depth_sensor_ultrasonic.distance

def left_DS_waitInRange():
    left_sensor_ultrasonic.wait_for_in_range()

def right_DS_waitInRange():
    right_sensor_ultrasonic.wait_for_in_range()





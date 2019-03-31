# uses ultrasonic sensor within the receptacle
# to look for a different distance

ERROR_THRESHOLD = 0.1
EMPTY_RECEPTACLE_DIST = 0.3

LEFT_ECHO_PIN = 14
LEFT_TRIG_PIN = 15

RIGHT_ECHO_PIN = 19
RIGHT_TRIG_PIN = 26

DEPTH_ECHO_PIN = 9
DEPTH_TRIG_PIN = 11


left_sensor_ultrasonic = DistanceSensor(echo = LEFT_ECHO_PIN, trigger = LEFT_TRIG_PIN, threshold_distance = THRESHOLD_DIST)
right_sensor_ultrasonic = DistanceSensor(echo = RIGHT_ECHO_PIN, trigger = RIGHT_TRIG_PIN, threshold_distance = THRESHOLD_DIST)
motion_sensor_ultrasonic = DistanceSensor(echo = MOTION_ECHO_PIN, trigger = MOTION_TRIG_PIN, threshold_distance = THRESHOLD_DIST)


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




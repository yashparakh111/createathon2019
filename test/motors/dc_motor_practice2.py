# Filename: motor_practice.py
# UT Create-a-Thon 2019
# Purpose: To practice interfacing DC motors to Raspberry Pi

import time
#import RPi.GPIO as GPIO
from gpiozero import *

# Declare pins for each output
PWMA = 4
PWMB = 22
AIN1 = 18
AIN2 = 17
BIN1 = 3
BIN2 = 23
STBY = 27
'''
PWMA = 7
PWMB = 15
AIN1 = 12
AIN2 = 11
BIN1 = 5
BIN2 = 16
STBY = 13
'''

motorA = Motor(forward = AIN1, backward = AIN2)
motorB = Motor(forward = BIN1, backward = BIN2)
PWM_motor_A = PWMOutputDevice(pin = PWMA, frequency = 2000)
PWM_motor_B = PWMOutputDevice(pin = PWMB, frequency = 2000)

print("Motors initialized")
PWM_motor_A.on()
PWM_motor_B.on()

print("Motors moving forward")
# TEST 1: Going Forward at Full Speed
motorA.forward()
motorB.forward()
time.sleep(5)

print("Motor moving backwards")
# TEST 2: Going Backward at Full Speed
motorA.backward()
motorB.backward()
time.sleep(5)

# STOP MOTORS
motorA.stop()
motorB.stop()

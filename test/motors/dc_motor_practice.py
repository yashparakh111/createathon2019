# Filename: motor_practice.py
# UT Create-a-Thon 2019
# Purpose: To practice interfacing DC motors to Raspberry Pi

import time
import RPi.GPIO as GPIO
#from gpiozero import *

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)

# Declare pins for each output
# Setup the GPIO pins
PWMA = 4        # GPIO pin layout
PWMB = 22
AIN1 = 18
AIN2 = 17
BIN1 = 3
BIN2 = 23
STBY = 27
'''
PWMA = 7        # Board pin layout
PWMB = 15
AIN1 = 12
AIN2 = 11
BIN1 = 5
BIN2 = 16
STBY = 13
'''
# Setup the GPIO pins
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)

# ********** TEST 1 ************
# Drive each motor clockwise for 5 seconds
GPIO.output(AIN1, GPIO.HIGH)		# Set direction
GPIO.output(AIN2, GPIO.LOW)
GPIO.output(BIN1, GPIO.HIGH)
GPIO.output(BIN2, GPIO.LOW)

GPIO.output(PWMA, GPIO.HIGH)		# Set speed
GPIO.output(PWMB, GPIO.HIGH)

GPIO.output(STBY, GPIO.HIGH)		# Disable STBY
time.sleep(5)						# Go for 5 seconds

# ********** TEST 2 ************
# Drive each motor counterclockwise for 5 seconds
GPIO.output(AIN1, GPIO.LOW)			# Set direction
GPIO.output(AIN2, GPIO.HIGH)
GPIO.output(BIN1, GPIO.LOW)
GPIO.output(BIN2, GPIO.HIGH)
time.sleep(5)

# ********** STOP **************
GPIO.output(PWMA, GPIO.LOW)
GPIO.output(PWMB, GPIO.LOW)
GPIO.output(AIN2, GPIO.LOW)
GPIO.output(BIN2, GPIO.LOW)

GPIO.cleanup()

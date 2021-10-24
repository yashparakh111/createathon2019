# Filename: Motor_Controller.py
# UT Create-a-Thon 2019
# Purpose: Provides methods for controlling the servos and DC motors

from time import sleep
from gpiozero import *

# ************** PIN INIT ***************
# Motor A
PWMA = 4 
AIN1 = 18
AIN2 = 17
MOTORA = Motor(forward = AIN1, backward = AIN2)
PWM_MOTOR_A = PWMOutputDevice(pin = PWMA, frequency = 2000)
PWM_MOTOR_A.on()

# Motor B
BIN1 = 3
BIN2 = 23
PWMB = 22
STBY = 27
MOTORB = Motor(forward = BIN2, backward = BIN1)
PWM_MOTOR_B = PWMOutputDevice(pin = PWMB, frequency = 2000)
PWM_MOTOR_B.on()

# Motor C
PWMC = 5 
CIN1 = 6
CIN2 = 13
MOTORC = Motor(forward = CIN1, backward = CIN2)
PWM_MOTOR_C = PWMOutputDevice(pin = PWMC, frequency = 2000)
PWM_MOTOR_C.on()

# Motor D
DIN1 = 20
DIN2 = 21
PWMD = 2
MOTORD = Motor(forward = DIN2, backward = DIN1)
PWM_MOTOR_D = PWMOutputDevice(pin = PWMD, frequency = 2000)
PWM_MOTOR_D.on()


# Servo General
LOW_DUTY_CYCLE = 4
HIGH_DUTY_CYCLE = 30

# Servo Left 1
SERVOL1_PIN = 25
SERVOL1 = PWMOutputDevice(pin = SERVOL1_PIN, initial_value = 0.08, frequency = 100)     # Initial position is 0 degrees

# Servo Left 2
SERVOL2_PIN = 8
SERVOL2 = PWMOutputDevice(pin = SERVOL2_PIN, initial_value = 0.08, frequency = 100)

# Servo Right 1
SERVOR1_PIN = 7
SERVOR1 = PWMOutputDevice(pin = SERVOR1_PIN, initial_value = 0.21, frequency = 100)

# Servo Right 2
SERVOR2_PIN = 16
SERVOR2 = PWMOutputDevice(pin = SERVOR2_PIN, initial_value = 0.21, frequency = 100)



# Move trash recepticle to the left
def moveReceptacleLeft():
    MOTORA.forward()
    MOTORB.forward()
    MOTORC.backward()
    MOTORD.backward()

# Move trash recepticle to the right
def moveReceptacleRight():
    MOTORA.backward()
    MOTORB.backward()
    MOTORC.forward()
    MOTORD.forward()

# Stop the trash recepticle
def stopReceptacle():
    MOTORA.stop()
    MOTORB.stop()
    MOTORC.stop()
    MOTORD.stop()


# Open the recepticle flaps
def openFlaps():
    SERVOL1.value = 0.15
    SERVOL2.value = 0.15
    SERVOR1.value = 0.15
    SERVOR2.value = 0.15

# Close the recepticle flaps
def closeFlaps():
    SERVOL1.value = 0.08
    SERVOL2.value = 0.08
    SERVOR1.value = 0.21
    SERVOR2.value = 0.21


# Open and close flap
def flapMotion():
    openFlaps()
    sleep(1)
    closeFlaps()

import RPi.GPIO as GPIO
import time

RIGHT_SERVO_2_PIN = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RIGHT_SERVO_2_PIN, GPIO.OUT)

p = GPIO.PWM(RIGHT_SERVO_2_PIN, 50)
p.start(2.5)

try:
    while True:
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(12.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(0.5)

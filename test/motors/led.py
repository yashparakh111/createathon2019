from gpiozero import *
import time

led = PWMLED(7, frequency = 1)

while True:
    led.value = 0
    time.sleep(2)
    led.value = 0.25
    time.sleep(2)
    led.value = 1
    time.sleep(1)

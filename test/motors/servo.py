from gpiozero import *
import time

RIGHT_SERVO_2_PIN = 7
freq = 100

right_servo_2 = PWMOutputDevice(pin = RIGHT_SERVO_2_PIN, initial_value = 0, frequency = freq)

print("Servo Pin Initialized")

low_duty_cycle = 4
high_duty_cycle = 30
multiplier = 0.01

# 50 Hz: 0% to 12% (2.4 ms)
# 100 Hz: 8% - 15% - 21% (0, 90, 180)

try: 
    for i in range(low_duty_cycle, high_duty_cycle, 1):
        duty_cycle = multiplier * i
        print("Duty Cycle: ", str(duty_cycle))
        right_servo_2.value = duty_cycle
        time.sleep(1)

    for i in range(high_duty_cycle, low_duty_cycle, -1):
        duty_cycle = multiplier * i
        print("Duty Cycle: ", str(duty_cycle))
        right_servo_2.value = duty_cycle
        time.sleep(1)

        #freq = freq + 10
        #p.stop()
        #p = GPIO.PWM(RIGHT_SERVO_2_PIN, freq)
        #print("Freq: ", str(freq))
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

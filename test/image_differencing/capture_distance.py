from gpiozero import DistanceSensor

echo = 17
trigger = 4

compartment_ultrasonic = DistanceSensor(echo, trigger)

ultrasonic.distance

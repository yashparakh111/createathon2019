# Filename: LED_practice.py
# UT Create-a-Thon 2019
# Purpose: To set a string of LEDs to white for 5 sec.

from neopixel import *
import time
from something import *

# LED strip configuration:
LED_COUNT = 120         # Number of LEDs to light up in string
LED_PIN = 12            # GPIO pin used for the LED pins
LED_FREQ_HZ = 800000    # LED signal frequency in hertz
LED_DMA = 10            # DMA channel to use for generating signal
LED_INVERT = 0          # Always zero
LED_BRIGHTNESS = 255    # Integer from 0 to 255 with 0 being off and 255 being brightest
LED_CHANNEL = 0         # set to 1 for GPIOs 13, 19, 41, 45, 53

def colorWipe(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()           # Initialize the library
colorWipe(strip, Color(127, 127, 127))
time.sleep(5)
colorWipe(strip, Color(0, 0, 0))

HelloWorld()

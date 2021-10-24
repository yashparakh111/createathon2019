# Filename: LED_practice.py
# UT Create-a-Thon 2019
# Purpose: To set a string of LEDs to white for 5 sec.
'''
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

strip = NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()           # Initialize the library
colorWipe(strip, Color(127, 127, 127))
time.sleep(5)
colorWipe(strip, Color(0, 0, 0))

HelloWorld()

'''


# Filename: LED_Controller.py
# UT Create-a-Thon 2019
# Purpose: To set a string of LEDs to white for 5 sec.

#from neopixel import *
import neopixel
import board
import time

# ***************** CONFIGURATION ********************* 
# General Info
LED_FREQ_HZ = 800000        # LED signal frequency in hertz
LED_DMA = 10                # DMA channel to use for generating signal
LED_INVERT = 0              # Always zero
LED_CHANNEL = 0             # Set to 1 for GPIOs 13, 19, 41, 45, 53
ORDER = neopixel.GRB

# LED Strip in Recepticle Compartment
COMP_LED_COUNT = 60         # Number of LEDs in the strip
#COMP_LED_PIN = 12           # GPIO pin used
COMP_LED_PIN = board.D12           # GPIO pin used
COMP_LED_BRIGHTNESS = 255   # Brightness of LED strip, 0 is off and 255 is the brightest
#COMP_STRIP = Adafruit_NeoPixel(COMP_LED_COUNT, COMP_LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, COMP_LED_BRIGHTNESS, LED_CHANNEL)        # Create object for LED strip in the recpeticle compartment
COMP_STRIP = neopixel.NeoPixel(COMP_LED_PIN, COMP_LED_COUNT, brightness = 1, auto_write = False, pixel_order = ORDER)
#COMP_STRIP.begin()          # Initialize the library

'''
# LED Strips in Bin Chasis
BIN_LED_COUNT = 120         # Number of LEDs in the strip(s)
#BIN_LED_PIN = 20            # GPIO pin used
BIN_LED_PIN = board.D
BIN_LED_BRIGHTNESS = 255    # Brightness of LED strip(s), 0 is off and 255 is the brightest
#BIN_STRIP = Adafruit_NeoPixel(COMP_LED_COUNT, COMP_LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, COMP_LED_BRIGHTNESS, LED_CHANNEL)        # Create object for LED strip in the bin chasis
BIN_STRIP = neopizel.NeoPixel(BIN_LED_PIN, COMP_LED_COUNT, brightness = 1, auto_write = False, pixel_order = ORDER)
BIN_STRIP.begin()           # Initialize the library
ANIMATE_TIME = 10           # Amount of time that LED stip(s) are on and animating during classification
'''



# Helper function to set LEDs all to a specific color
# Only to be used within this file
def colorWipe(strip, color_num):
    #for i in range(strip.numPixels()):
        #strip.setPixelColor(i, color)
        #strip.show()
    COMP_STRIP.fill((color_num, color_num, color_num))


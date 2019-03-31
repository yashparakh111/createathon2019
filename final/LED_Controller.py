# Filename: LED_Controller.py
# UT Create-a-Thon 2019
# Purpose: To set a string of LEDs to white for 5 sec.

from neopixel import *
import time

# ***************** CONFIGURATION ********************* 
# General Info
LED_FREQ_HZ = 800000        # LED signal frequency in hertz
LED_DMA = 10                # DMA channel to use for generating signal
LED_INVERT = 0              # Always zero
LED_CHANNEL = 0             # Set to 1 for GPIOs 13, 19, 41, 45, 53

# LED Strip in Recepticle Compartment
COMP_LED_COUNT = 60         # Number of LEDs in the strip
COMP_LED_PIN = 12           # GPIO pin used
COMP_LED_BRIGHTNESS = 255   # Brightness of LED strip, 0 is off and 255 is the brightest
COMP_STRIP = Adafruit_NeoPixel(COMP_LED_COUNT, COMP_LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, COMP_LED_BRIGHTNESS, LED_CHANNEL)        # Create object for LED strip in the recpeticle compartment
COMP_STRIP.begin()          # Initialize the library

# LED Strips in Bin Chasis
BIN_LED_COUNT = 120         # Number of LEDs in the strip(s)
BIN_LED_PIN = 20            # GPIO pin used
BIN_LED_BRIGHTNESS = 255    # Brightness of LED strip(s), 0 is off and 255 is the brightest
BIN_STRIP = Adafruit_NeoPixel(COMP_LED_COUNT, COMP_LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, COMP_LED_BRIGHTNESS, LED_CHANNEL)        # Create object for LED strip in the bin chasis
BIN_STRIP.begin()           # Initialize the library
ANIMATE_TIME = 10           # Amount of time that LED stip(s) are on and animating during classification



# Helper function to set LEDs all to a specific color
# Only to be used within this file
def __colorWipe(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

# Lights the main trash recepticle compartment to a constant white
def lightCompartment():
    colorWipe(COMP_STRIP, Color(127, 127, 127))         # LEDs set to white

# Turns off the lights within the trash recepticle compartment
def compartmentOff():
    colorWipe(COMP_STRIP, Color(0, 0, 0))               # LEDs turned off

# Goes through animation sequence of LEDs in bin chasis when object is being classified
def animateBin():
    for i in range(ANIMATE_TIME):
        for j in range(3):
            for k in range(0, BIN_STRIP.numPixels(), 3):
                strip.setPixelColor(i + j, Color(0, 0, 0))
            strip.show()
            time.sleep(50/1000.0)
            for k in range(0, BIN_STRIP.numPixels(), 3):
                strip.setPixelColor(j + k, 0)

    colorWipe(BIN_STRIP, Color(0, 0, 0))                # Turn off LEDs

# Kill switch for all LED strips
def killLED():
    colorWipe(COMP_STRIP, Color(0, 0, 0))
    colorWipe(BIN_STRIP, Color(0, 0, 0))

import Game


import time
import serial
import RPi.GPIO as GPIO
import io
from dotstar import Adafruit_DotStar


def init():

    global gridPixels 

    gridPixels = 72 # Number of LEDs in strip

    # Here's how to control the strip from any two GPIO pins:
    global gridDatapin
    gridDatapin  = 20
    global gridClockpin
    gridClockpin = 21
    global gridStrip
    gridStrip    = Adafruit_DotStar(gridPixels, gridDatapin, gridClockpin)

    gridStrip.begin()           # Initialize pins for output
    gridStrip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

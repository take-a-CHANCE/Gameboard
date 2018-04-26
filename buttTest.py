import RPi.GPIO as GPIO
import time
import io
from dotstar import Adafruit_DotStar

gridPixels = 72 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
gridDatapin  = 20
gridClockpin = 21
gridStrip    = Adafruit_DotStar(gridPixels, gridDatapin, gridClockpin)

gridStrip.begin()           # Initialize pins for output
gridStrip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

GPIO.setmode(GPIO.BCM)

chanList=[2,3,4,5,6,7,8,9]

GPIO.setup(chanList, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if not GPIO.input(2):
        print "Pressed 0"
    elif not GPIO.input(3):
        print "Pressed 1"
    elif not GPIO.input(4):
        print "Pressed 2"
    elif not GPIO.input(5):
        print "Pressed 3"
    elif not GPIO.input(6):
        print "Pressed 4"
    elif not GPIO.input(7):
        print "Pressed 5"
    elif not GPIO.input(8):
        print "Pressed 6"
    elif not GPIO.input(9):
        print "Pressed 7"
    time.sleep(0.05)
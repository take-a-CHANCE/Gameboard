import time
import serial
from dotstar import Adafruit_DotStar

numpixels = 30 # Number of LEDs in strip
#this is a tests
# Here's how to control the strip from any two GPIO pins:
datapin  = 23
clockpin = 24
strip    = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()           # Initialize pins for output
strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

state=1

while(1):
    if(state==1):       # Waiting on input
        state=2
        exit()
    if(state==2):       # Process changes to board
        state=3
        exit()
    if(state==3):       # send updated board
        state=1
        exit()


def updateBoard():
    exit()

def sendUpdate():
    exit()

def recvUpdate(): 
    exit()

def getButtonPress():
    exit()
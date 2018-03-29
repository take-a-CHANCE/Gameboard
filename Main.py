import time
import serial
from dotstar import Adafruit_DotStar

numpixels = 80 # Number of LEDs in strip
#this is a test
# Here's how to control the strip from any two GPIO pins:
datapin  = 20
clockpin = 26
strip    = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()           # Initialize pins for output
strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

state=1

# Board datastructure (array?)

#  Row |    #   #   #   #   #   #   #   #   #
#      |Col A   B   C   D   E   F   G   H  Status   
#   1  |    0   1   2   3   4   5   6   7  79
#   2  |    8   9  10  11  12  13  14  15  78
#   3  |   16  17  18  19  20  21  22  23  77
#   4  |   24  25  26  27  28  29  30  31  76
#   5  |   32  33  34  35  36  37  38  39  75
#   6  |   40  41  42  43  44  45  46  47  74
#   7  |   48  49  50  51  52  53  54  55  73
#   8  |   56  57  58  59  60  61  62  63  72
# Stat |   64  65  66  67  68  69  70  71  **


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
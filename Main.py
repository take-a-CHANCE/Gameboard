import Game


import time
import serial
import RPi.GPIO as GPIO
import io
from dotstar import Adafruit_DotStar

gridPixels = 72 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
gridDatapin  = 20
gridClockpin = 21
gridStrip    = Adafruit_DotStar(gridPixels, gridDatapin, gridClockpin)

gridStrip.begin()           # Initialize pins for output
gridStrip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

channel = 3

GPIO.setmode(GPIO.BCM)

# statusPixels = 16
# statusDatapin = 19
# statusClockPin = 26

# statusStrip = Adafruit_DotStar(statusPixels, statusDatapin, statusClockPin)
# statusStrip.begin()


state=1

# Board datastructure (array?)

#  Row |    #   #   #   #   #   #   #   #  
#      |    A   B   C   D   E   F   G   H     
#   1  |    0   1   2   3   4   5   6   7  
#   2  |    8   9  10  11  12  13  14  15  
#   3  |   16  17  18  19  20  21  22  23  
#   4  |   24  25  26  27  28  29  30  31  
#   5  |   32  33  34  35  36  37  38  39  
#   6  |   40  41  42  43  44  45  46  47  
#   7  |   48  49  50  51  52  53  54  55  
#   8  |   56  57  58  59  60  61  62  63  


# Status datastructure

#  Row |    #   #   #   #   #   #   #   #   #
#      |  Stat  A   B   C   D   E   F   G   H     
#   1  |    0   *   *   *   *   *   *   *   *
#   2  |    1   *   *   *   *   *   *   *   *
#   3  |    2   *   *   *   *   *   *   *   * 
#   4  |    3   *   *   *   *   *   *   *   * 
#   5  |    4   *   *   *   *   *   *   *   *
#   6  |    5   *   *   *   *   *   *   *   * 
#   7  |    6   *   *   *   *   *   *   *   * 
#   8  |    7   *   *   *   *   *   *   *   *
# Stat |    *   8   9  10  11  12  13  14  15

#Structure for boats
#Code to create and run game
def main():
    
    theGame = Game.Game()
    theGame.run()

if __name__ == "__main__":
   main()


# while(1):
#     if(state==1):       # Waiting on input
#         state=2
#     if(state==2):       # Process changes to board and display them
#         state=3
#     if(state==3):       # send updated board
#         state=1

# Draws the updated gameboard
    

# Updates the status LEDs
# def updateStatus():
#     for i in range(0,7):
#         statusStrip.setPixelColor(i,0,0,255)
#     statusStrip.show()

# Sends the move to the arduino to send to the other board
def sendUpdate():
    exit()

# Pull the update from the arduino 
def recvUpdate(): 
    exit()

# Get the button press for the turn from the arduino
def getButtonPress():
    exit()
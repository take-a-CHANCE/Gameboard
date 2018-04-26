import RPi.GPIO as GPIO
#arduino setup
import serial
import time
#Arduino = serial.Serial("COM3", 9600)

from dotstar import Adafruit_DotStar

shipType = dict(Carrier =  5, Battleship = 4, Cruiser = 3, Submarine = 2, Destroyer = 1)

gridPixels = 72


# Here's how to control the strip from any two GPIO pins:
gridDatapin  = 20
gridClockpin = 21
gridStrip    = Adafruit_DotStar(gridPixels, gridDatapin, gridClockpin)

gridStrip.begin()           # Initialize pins for output
gridStrip.setBrightness(64) # Limit brightness to ~1/4 duty cycle


#
# Ship
#
shipType = dict(Carrier =  5, Battleship = 4, Cruiser = 3, Submarine = 2, Destroyer = 1)
class Ship(object):
    '''A ship object'''
    def __init__(self, type, posY, posX, orientation):
        if type == "Carrier":
            self.__m_type = shipType['Carrier']
            self.__m_hitpoints = shipType['Carrier']
        elif type == "Battleship":
            self.__m_type = shipType['Battleship']
            self.__m_hitpoints = shipType['Battleship']
        elif type == "Cruiser":
            self.__m_type = shipType['Cruiser']
            self.__m_hitpoints = shipType['Cruiser']
        elif type == "Submarine":
            self.__m_type = shipType['Submarine']
            self.__m_hitpoints = shipType['Submarine']
        elif type == "Destroyer":
            self.__m_type = shipType['Destroyer']
            self.__m_hitpoints = shipType['Destroyer']
        self.__m_posY = posY
        self.__m_posX = posX
        self.__m_orientation = orientation
        #for print purposes
        self.__m_stype = type
        #ship size
        self.__m_size = self.__m_hitpoints

    def __str__(self):
        return self.__sm_type
    
    def takeDamage(self):
        self.__m_hitpoints = self.__m_hitpoints - 1 if self.__m_hitpoints > 0 else 0

    def lightUp(self):
        currentHP = self.__m_hitpoints
        if currentHP == self.getType
            position = self.getType + 63
            gridStrip.setPixelColor(position,255,0,0)
            gridStrip.show()

    @property
    def getType(self):
        return self.__m_type
    @property
    def getHitpoints(self):
        return self.__m_hitpoints
    @property
    def getX(self):
        return self.__m_posX
    @property
    def getY(self):
        return self.__m_posY
    @property
    def getSize(self):
        return self.__m_size
    @property
    def getOrientation(self):
        return self.__m_orientation
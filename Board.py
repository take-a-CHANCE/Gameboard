#
# Board of tiles
# has tiles and ships

import Tile
import Ship

import random
import RPi.GPIO as GPIO

import settings

import socket

from dotstar import Adafruit_DotStar

shipType = dict(Carrier =  5, Battleship = 4, Cruiser = 3, Submarine = 2, Destroyer = 1)
tileType = dict(empty = 0, ship = 1, hit = 2, miss = 3, hidden = 4)
boardType = dict(Player = 0, Enemy = 1)

boardHost = ["RPIboard1", "RPIboard2"]

# gridPixels = 72


# Here's how to control the strip from any two GPIO pins:
# gridDatapin  = 20
# gridClockpin = 21
# settings.gridStrip    = Adafruit_DotStar(gridPixels, gridDatapin, gridClockpin)

# settings.gridStrip.begin()           # Initialize pins for output
# settings.gridStrip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

GPIO.setmode(GPIO.BCM)

chanList=[2,3,4,5,6,7,8,9]

GPIO.setup(chanList, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class Board(object):
    '''Board of tile objects'''
    #constructor
    def __init__(self, type):
        #member vars
        #private
        self.__m_width = 8
        self.__m_height = 8
        self.__m_type = type
        self.__m_Ships = list()
        #public
        self.m_Board = [[]]
        #init Board
        for i in range(0, self.__getHeight):
            self.m_Board.append([])
            for j in range(0, self.__getWidth):
                #init all to blank
                self.m_Board[i].append(Tile.Tile(tileType['empty']))
        if type == boardType["Player"] or type == boardType["Enemy"]:
            shipType = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
            
            #Ship Position presets for player and 'enemy'
            if socket.gethostname() == boardHost[0]:
                aiships = [(0,0,"v"), (0,2,"h"), (7,0,"h"), (3,6,"h"), (0,7,"v")]
            elif socket.gethostname() == boardHost[1]:
                aiships = [(3,0,'h'), (4,7,'v'), (6,1,'h'), (4,1,'v'), (1,5,'v')]

            
            while len(shipType) > 0:
                ship = aiships.pop()
                posY = ship[0]  
                posX = ship[1]
                orientation = ship[2]

            #add ship to fleet
                self.__m_Ships.append(Ship.Ship(shipType[-1], posY, posX, orientation))
                #add on map
                size = self.__m_Ships[-1].getHitpoints

                #if player show hull, if enemy hide
                if type == boardType['Player']:
                    shipHull = tileType['hidden']
                else:
                    shipHull = tileType['hidden']

                while size > 0:
                    if orientation == "h":
                        self.m_Board[posY][posX+size-1].setTile(shipHull)
                    else:                        
                        self.m_Board[posY+size-1][posX].setTile(shipHull)
                    size -= 1
                #remove last ship from ship list
                shipType.pop(-1)

    def __str__(self):
        labelLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        labelNumbers = [0, 1, 2, 3, 4, 5, 6, 7]
        rep = " "
        for number in labelNumbers:
            rep += str(number)
        for i in range(0, self.__getHeight):
            rep += '\n'
            rep += labelLetters[i]
            for j in range(0, self.__getWidth):
                chosenTileType = self.m_Board[i][j].getType[0]
                rep += chosenTileType
                red = 0
                green = 0
                blue = 0
                if chosenTileType == 'W':
                    blue = 255
                elif chosenTileType == 'X':
                    red = 255
                LEDNum = i*8 + j
                if LEDNum > 60:
                    print LEDNum
                settings.gridStrip.setPixelColor(LEDNum,green,red,blue)
        rep += '\n'
        settings.gridStrip.show()
        return rep



    @property
    def __getWidth(self):
        return self.__m_width
    @property
    def __getHeight(self):
        return self.__m_height


    def getTile(self, y, x):
        return self.m_Board[int(y)][int(x)]

    def setTile(self, y, x, tile):
        self.m_Board[y][x] = tile

    @staticmethod
    def letterToNumber(letter):
        labelLetters = ['A','B','C','D','E','F','G','H']
        number = 0
        for l in labelLetters:
            if l.lower() == letter.lower():
                break
            number += 1
        return number


    def getFleet(self):
        return self.__m_Ships

    @property
    def getFleetSize(self):
        return len(self.__m_Ships)


    def hit(self, y, x):
        #iterate through fleet
        for ship in self.__m_Ships:
            #find ship that was hit
            if int(x) >= ship.getX - ship.getSize and int(x) <= ship.getX + ship.getSize:
                if int(y) >= ship.getY - ship.getSize and int(y) <= ship.getY + ship.getSize:
                    #found ship
                    ship.takeDamage()
                    hitpoints = ship.getHitpoints
                    selectShipType = ship.getType
                    if (hitpoints == 0):
                        self.__m_Ships.remove(ship)
                        fleetSize = len(self.__m_Ships)
                        print self.__m_Ships
                        if fleetSize == 0:
                            return True
    


    def light(self, y, x):
        #iterate through fleet
        for ship in self.__m_Ships:
            #find ship that was hit
            try:
                if int(x) >= ship.getX - ship.getSize and int(x) <= ship.getX + ship.getSize:
                    if int(y) >= ship.getY - ship.getSize and int(y) <= ship.getY + ship.getSize:
                        #found ship
                        hitpoints = ship.getHitpoints
                        selectShipType = ship.getType
                        if (hitpoints == 0):
                            if selectShipType == 1:
                                settings.gridStrip.setPixelColor(64,0,255,0)
                            if selectShipType == 2:
                                settings.gridStrip.setPixelColor(65,0,255,0)
                            if selectShipType == 3:
                                settings.gridStrip.setPixelColor(66,0,255,0)
                            if selectShipType == 4:
                                settings.gridStrip.setPixelColor(67,0,255,0)
                            if selectShipType == 5:
                                settings.gridStrip.setPixelColor(68,0,255,0)
                            settings.gridStrip.show()
                            self.__m_Ships.remove(ship)
                            fleetSize = len(self.__m_Ships)
                            if fleetSize == 0:
                                return True
            except:
                return False
                            
                            
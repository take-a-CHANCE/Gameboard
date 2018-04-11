#
# Board of tiles
# has tiles and ships

import Tile
import Ship

import random

tileType = dict(empty = 0, ship = 1, hit = 2, miss = 3, hidden = 4)
boardType = dict(Player = 0, Enemy = 1)

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
            if type == boardType["Player"]:
                aiships = [(0,0,"v"), (0,2,"h"), (6,0,"v"), (3,6,"v"), (0,7,"v")]
            elif type == boardType["Enemy"]:
                aiships = [(3,2,"v"), (9,2,"h"), (5,0,"v"), (3,6,"h"), (7,7,"v")]


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
                    shipHull = tileType['ship']
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
                rep += self.m_Board[i][j].getType[0]
        rep += '\n'
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
                    if (hitpoints == 0):
                        self.__m_Ships.remove(ship)
                        fleetSize = len(self.__m_Ships)
                        #if fleetSize > 0:
                            #print("Ship destroyed! {} ships remaining".format(fleetSize))
                            #ship is destroyed
                        #else:
                            #Game over, fleet destroyed
                         #   return True
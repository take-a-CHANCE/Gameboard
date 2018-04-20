#
# Game class
# has 2 boards, one for the player one for the Ai
#
import Board
import random

#arduino setup
import serial
import time
Arduino = serial.Serial("COM3", 9600)

shipType = dict(Carrier =  5, Battleship = 4, Cruiser = 3, Submarine = 2, Destroyer = 1)
tileType = dict(empty = 0, ship = 1, hit = 2, miss = 3, hidden = 4)
boardType = dict(Player = 0, Enemy = 1)


class Game(object):
    ''' Game Class '''
    def __init__(self):
        self.__m_brunning = True
        self.__m_turn = 0
        self.m_pBoard = 0
        self.m_eBoard = 0

    def __str__(self):
        rep = "<Battleship Game>"
        return rep
    
    @property
    def __isRunning(self):
        return self.__m_brunning

    def __setRunning(self, boolean):
        self.__m_brunning = boolean

    def run(self):
        print("Loading please wait...")
        #give the Arduino time to connect
        time.sleep(3)
        import os
        os.system("cls")

        #inform Arduino of game status: on 1 red led, off 0 blue led
        if Arduino.isOpen():
            Arduino.write('1'.encode())

        #generate player and enemy boards
        self.m_pBoard = Board.Board(boardType["Player"])
        #add 5 ships to the board
        self.m_eBoard = Board.Board(boardType["Enemy"])
        #game loop
        while self.__isRunning:
            #print board and menu
            print("Player Board: \n{}".format(self.m_pBoard))
            print("Enemy Board: \n{}".format(self.m_eBoard))
            if (self.__m_turn % 2 == 0):
                uInput = input()
                if int(uInput) == 0:
                    endgame = True
                else:
                    uInput = input("Call your shot!(ex:C5): ")
                    endgame = self.shoot(self.letterToNumber(uInput[0]), uInput[1])
                    #delete input
                    del uInput
            #cpu turn
            else:
                posY = random.randrange(0,10,1)
                posX = random.randrange(0,10,1)
                endgame = self.shoot(posY, posX)

            if endgame:
                if int(uInput) != 0:
                    print("Winner is player {}!".format((self.__m_turn % 2) + 1))
                self.__m_brunning = False    
                #inform Arduino that game is over
                Arduino.write("0".encode())
            else:                
                self.__m_turn += 1

    def shoot(self, y, x):
        ended = False
        #player
        if self.__m_turn % 2 == 0:
            tile = self.m_eBoard.getTile(y, x)
        #cpu
        else:
            tile = self.m_pBoard.getTile(y, x)
        tileType = tile.getType
        tileType = tileType[1] if len(tileType) > 1 else 0
#test types
#        print(type(tileType), type(TILE_TYPE["EMPTY"]))
#        print(tileType, TILE_TYPE["EMPTY"])
#end test
        if tileType == tileType["empty"]:
            print("Shot Missed!")
            tile.setTile(tileType["miss"])
        elif tileType == tileType["hidden"] or tileType == tileType["ship"]:
            print("Shot Hit!")
            tile.setTile(tileType["hit"])
            #only on player turn
            if self.__m_turn % 2 == 0:
                #figure out what ship we hit
                shipType = 0

                for ship in self.m_eBoard.getFleet():
                    shipX = int(ship.getX)
                    shipY = int(ship.getY)
                    x = int(x)
                    y = int(y)
                    size = ship.getSize
                    orientation = ship.getOrientation
                    if orientation == 'h':
                        if x >= shipX and x <= shipX + size:
                            if y == shipY:
                                #hit, get ship type
                                shipType = int(ship.getType)

                    elif orientation == 'v':
                        if y >= shipY and y <= shipY + size:
                            if x == shipX:
                                #hit
                                shipType = int(ship.getType)
                #when we hit, send ship info to Arduino
                if shipType == shipType['Destroyer']:
                    Arduino.write("2".encode())
                    print("hit Destroyer")
                if shipType == shipType['Submarine']:
                    Arduino.write("3".encode())
                    print("hit Submarine")
                if shipType == shipType['Cruiser']:
                    Arduino.write("4".encode())
                    print("hit Cruiser")
                if shipType == shipType['Battleship']:
                    Arduino.write("5".encode())
                    print("hit Battleship")
                if shipType == shipType['Carrier']:
                    Arduino.write("6".encode())
                    print("hit Carrier")
                #end Arduino
            ended = self.m_eBoard.hit(y, x)
        else:
            print("Already fired there! Obvious miss!")
        return ended

    @staticmethod
    def letterToNumber(letter):
        labelLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        number = 0
        for l in labelLetters:
            if l.lower() == letter.lower():
                break
            number += 1
        return number
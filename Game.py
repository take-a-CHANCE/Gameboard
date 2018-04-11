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
import serial
import RPi.GPIO as GPIO
import time
import io
from dotstar import Adafruit_DotStar

gridPixels = 30 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
gridDatapin  = 28
gridClockpin = 29
gridStrip    = Adafruit_DotStar(gridPixels, gridDatapin, gridClockpin)

gridStrip.begin()           # Initialize pins for output
gridStrip.setBrightness(64) # Limit brightness to ~1/4 duty cycle


channel=5

GPIO.setmode(GPIO.BOARD)

ser=serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))

GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)



while 1:
    if not GPIO.input(channel):
        ser.write('Drew LEDs\n'.encode('utf-8'))
        ser.flush()
        print "Wrote data\n"
        for i in range(0,63):
            gridStrip.setPixelColor(i,255,0,0)
        gridStrip.show()
    
    elif ser.in_waiting:
        rcv=ser.readline()
        print "Received: "+rcv
        sio.flush()
        for i in range(0,63):
            gridStrip.setPixelColor(i,0,0,255)
        gridStrip.show()
    time.sleep(0.1)


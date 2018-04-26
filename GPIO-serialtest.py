import serial
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


channel=3

GPIO.setmode(GPIO.BCM)

ser=serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))

GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count=0

while 1:
    if not GPIO.input(channel):
        snt="A0"
        ser.write(snt+'\n'.encode('utf-8'))
        ser.flush()
        print "Wrote" + snt+ "\n"
        if count>71:
            count=0
            for i in range(0,72):
                gridStrip.setPixelColor(i,0,0,0)
            gridStrip.show()
        gridStrip.setPixelColor(count,255,0,0)
        gridStrip.show()
        count+=1
    
    elif ser.in_waiting:
        rcv=ser.readline()
        print "Received: "+rcv
        if "OK" not in rcv:
            ser.write('h\n')
        ser.flush()
        #sio.flush()
        if count>71:
            count=0
            for i in range(0,72):
                gridStrip.setPixelColor(i,0,0,0)
            gridStrip.show()
        gridStrip.setPixelColor(count,0,0,255)
        gridStrip.show()
        count+=1
    time.sleep(0.1)


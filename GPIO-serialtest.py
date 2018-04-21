import serial
import RPi.GPIO as GPIO
import time
import io


channel=5

GPIO.setmode(GPIO.BOARD)

ser=serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))

GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)



while 1:
    if not GPIO.input(channel):
        sio.write("test\n")
        print "Wrote data\n"
    
    elif ser.in_waiting:
        rcv=sio.readline()
        print "Received: "+rcv
        sio.flush()
    time.sleep(0.1)


import serial
import RPi.GPIO as GPIO
import time


channel=5

GPIO.setmode(GPIO.BOARD)

ser=serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while 1:
    if not GPIO.input(channel):
        ser.write("test\n")
        print("Wrote data\n")
    time.sleep(0.01)
    else:
        rcv=ser.readline()
        print("Received: "+rcv)


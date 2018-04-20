import serial
import RPi.GPIO as GPIO

channel=5

GPIO.setmode(GPIO.BOARD)

ser=serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while true:
    if GPIO.input(channel):
        ser.write("test\n")


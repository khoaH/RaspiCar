#!/usr/bin/python
import robot
from RPi import GPIO
from time import sleep
import RPi.GPIO as IO

GPIO.setmode(GPIO.BCM)

left_sensor = 11
right_sensor = 9

GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)

try:
    while True:
        if GPIO.input(left_sensor):
            robot.left(0.2)
            print("re trai")
        elif GPIO.input(right_sensor):
            robot.right(0.2)
            print("re phai")
        else:
            print("Following the line!")
            robot.forward(5)
except:
    GPIO.cleanup()



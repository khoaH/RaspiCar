#!/usr/bin/python
import robot
from RPi import GPIO
import time
import RPi.GPIO as IO

GPIO.setmode(GPIO.BCM)

left_sensor = 11
right_sensor = 9

GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)

try:
    while True:
        if GPIO.input(left_sensor):
            
            robot.left(0.1)
            
            print("re trai")
        elif GPIO.input(right_sensor):
            
            robot.right(0.1)
            
            #time.sleep(0.1)
            print("re phai")
        elif not (GPIO.input(left_sensor) and GPIO.input(right_sensor)):
            print("Following the line!")
            robot.forward(0.01)
        elif (GPIO.input(left_sensor) and GPIO.input(right_sensor)):
            robot.stop_forward(5)
except KeyboardInterrupt:
    GPIO.cleanup()



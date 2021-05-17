#! / usr / bin / python3
# coding = utf -8
# Auto.py file, part 1
from time import sleep
import RPi.GPIO as GPIO
import sys
import servoNJt as servo
import time
import threading
from threading import Thread
import ultrasonic_2 as usc

class KhoaThread(Thread):
    def __init__(self):
        super(KhoaThread,self).__init__()
    def run(self):  
        while(1):
            print(usc.distanceReturn())
            if usc.distanceReturn() < 60:
                print("Stop")
                break
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
EnableA = 13
EnableB = 19
Input1 = 17 #phai tien
Input2 = 22 #phai lui
Input3 =18 #trai tien 
Input4 = 23 #trai lui
speed1 = 40 #nhe
speed2 = 80 #manh
speed3 = 100 #thang
whiteFlag = 'True'

# the two line followers(r) real and(l) inks
# lf_r = 18
# lf_l = 22
GPIO.setup(EnableA, GPIO.OUT)
GPIO.setup(EnableB, GPIO.OUT)
GPIO.setup(Input1, GPIO.OUT)
GPIO.setup(Input2, GPIO.OUT)
GPIO.setup(Input3, GPIO.OUT)
GPIO.setup(Input4, GPIO.OUT)
# GPIO.setup(lf_l, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(lf_r, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
pwmA = GPIO.PWM(EnableA, 100)
pwmB = GPIO.PWM(EnableB, 100)


center_sensor= 16 #S3
left_sensor = 1  #S2
max_left_sensor = 7  #S1
right_sensor = 20 #S4
max_right_sensor= 21 #S5

GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)
GPIO.setup(max_left_sensor, GPIO.IN)
GPIO.setup(max_right_sensor, GPIO.IN)
GPIO.setup(center_sensor, GPIO.IN)

ultrathread= KhoaThread()
ultrathread.start()

# Function for driving straight ahead
def forward(speed):
    pwmA.start(speed)
    pwmB.start(speed)    
    GPIO.output(Input3, True)
    GPIO.output(Input4, False)
    GPIO.output(Input1, True)
    GPIO.output(Input2, False)
# Function for driving straight ahead
def reverse(speed):
    pwmA.start(speed)
    pwmB.start(speed)    
    GPIO.output(Input3, False)
    GPIO.output(Input4, True)
    GPIO.output(Input1, False)
    GPIO.output(Input2, True)
# Function for stop
def stop():
    pwmA.start(0)
    pwmB.start(0)

# Left turn function
def left(speed):
    pwmA.start(speed)
    pwmB.start(speed)
    GPIO.output(Input1, True)
    GPIO.output(Input2, False)
    GPIO.output(Input3, False)
    GPIO.output(Input4, True)
# Function to turn right
def right(speed):
    pwmB.start(speed)
    pwmA.start(speed)
    GPIO.output(Input3, True)
    GPIO.output(Input4, False)
    GPIO.output(Input1, False)
    GPIO.output(Input2, True)
    
def only_right_wheel(speed):
    pwmB.start(0)
#     GPIO.output(Input3, True)
#     GPIO.output(Input4, False)
    pwmA.start(speed)
    GPIO.output(Input1, False)
    GPIO.output(Input2, True)

def only_left_wheel(speed):
    pwmB.start(speed)
    pwmA.start(0)
    GPIO.output(Input3, True)
    GPIO.output(Input4, False)
#     GPIO.output(Input1, False)
#     GPIO.output(Input2, True)

def diff_wheel(speed_left, speed_right):
    pwmB.start(speed_left)
    pwmA.start(speed_right)
    GPIO.output(Input3, True)
    GPIO.output(Input4, False)
    GPIO.output(Input1, True)
    GPIO.output(Input2, False)

    
# while True:
#     try:
#         s1= GPIO.input(max_left_sensor)
#         s2= GPIO.input(left_sensor)
#         s3= GPIO.input(center_sensor)
#         s4= GPIO.input(right_sensor)
#         s5= GPIO.input(max_right_sensor)
#         
# #         if s1 == 1 and s2 == 1 and s3 == 1 and s4 == 1 and s5 == 1:
# #             forward(speed1)
# 
#         if s1 == 1 and s2 == 1 and s3 == 0 and s4 == 1 and s5 == 1:
#             forward(speed2)
#             sleep(0.1)
#         if s1 == 1 and s2 == 0 and s3 == 1 and s4 == 1 and s5 == 1:
#             left(speed1)
#             whiteFlag = False
#         if s1 == 0 and s2 == 1 and s3 == 1 and s4 == 1 and s5 == 1:
#             left(speed2)
#             whiteFlag = False
#         if s1 == 1 and s2 == 1 and s3 == 1 and s4 == 0 and s5 == 1:
#             right(speed1)
#             whiteFlag = True
#         if s1 == 1 and s2 == 1 and s3 == 1 and s4 == 1 and s5 == 0:
#             right(speed2)
#             whiteFlag = True
#         if s1 == 1 and s2 == 1 and s3 == 0 and s4 == 0 and s5 == 1:
#             only_left_wheel(speed1)
#             whiteFlag = True
#         if s1 == 1 and s2 == 0 and s3 == 0 and s4 == 1 and s5 == 1:
#             only_right_wheel(speed1)
#             whiteFlag = False
#         if s1 == 0 and s2 == 0 and s3 == 0 and s4 == 1 and s5 == 1:
#             only_right_wheel(speed2)
#             whiteFlag = False
#         if s1 == 1 and s2 == 1 and s3 == 0 and s4 == 0 and s5 == 0:
#             only_left_wheel(speed2)
#             whiteFlag = True
#         if s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0 and s5 == 0:
#             stop()
#             break
#         if s1 == 1 and s2 == 1 and s3 == 1 and s4 == 1 and s5 == 1:
#             if whiteFlag:
#                 right(speed1)
#                 print('turn right')
#             else:
#                 left(speed1)
#                 print('turn left')
#         print(str(s1)+" "+str(s2)+" "+str(s3)+" "+str(s4)+" "+str(s5))
#         sleep(0.01)
#     except KeyboardInterrupt:
#         GPIO.cleanup()
#         sys.exit()
GPIO.cleanup()


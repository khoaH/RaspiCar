import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

fwdleft = 17
fwdright = 18
revleft = 22
revright = 23
EnableA = 13
EnableB = 19
GPIO.setup(EnableA, GPIO.OUT)
GPIO.setup(EnableB, GPIO.OUT)
pwmA = GPIO.PWM(EnableA, 100)
pwmB = GPIO.PWM(EnableB, 100)

motors = [fwdleft,fwdright,revleft,revright]

for item in motors:
    GPIO.setup(item, GPIO.OUT)
    
def reverse(i):
    GPIO.output(fwdright, True)
    GPIO.output(fwdleft, True)
    time.sleep(i)
    GPIO.output(fwdright, False)
    GPIO.output(fwdleft, False)
    
def left(i):
    GPIO.output(revright, True)
    GPIO.output(fwdleft, True)
    time.sleep(i)
    GPIO.output(revright, False)
    GPIO.output(fwdleft, False)

def right(i):
    GPIO.output(fwdright, True)
    GPIO.output(revleft, True)
    time.sleep(i)
    GPIO.output(fwdright, False)
    GPIO.output(revleft, False)

def forward(i):
    GPIO.output(revleft, True)
    GPIO.output(revright, True)
    time.sleep(i)
    GPIO.output(revleft, False)
    GPIO.output(revright, False)

def reverse2(i):
    GPIO.output(fwdright, True)
    GPIO.output(fwdleft, True)

def stop_reverse2(i):
    time.sleep(i)
    GPIO.output(fwdright, False)
    GPIO.output(fwdleft, False)
    
def left2(i):
    GPIO.output(revright, True)
    GPIO.output(fwdleft, True)

def stop_left2(i):
    time.sleep(i)
    GPIO.output(revright, False)
    GPIO.output(fwdleft, False)

def right2(i):
    GPIO.output(fwdright, True)
    GPIO.output(revleft, True)

def stop_right2(i):
    time.sleep(i)
    GPIO.output(fwdright, False)
    GPIO.output(revleft, False)

def forward2(i):
    GPIO.output(revleft, True)
    GPIO.output(revright, True)

def stop_foward2(i):
    time.sleep(i)
    GPIO.output(revleft, False)
    GPIO.output(revright, False)

def stop(i):
    GPIO.output(revleft, False)
    GPIO.output(revright, False)
    time.sleep(i)
    
try:
	print("R E A D Y")
	forward(1)
except KeyboardInterrupt:
	print("E X I T")
	GPIO.cleanup()
        
        
        
        
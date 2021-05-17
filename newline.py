#! / usr / bin / python3
# coding = utf -8
# Auto.py file, part 1
from time import sleep
import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
EnableA = 13
EnableB = 19
Input1 = 17 #phai tien
Input2 = 22 #phai lui
Input3 =18 #trai tien 
Input4 = 23 #trai lui
Speed1 = 90
speed2 = 100
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



# Function for driving straight ahead
def forward(speed):
    pwmA.start(speed)
    pwmB.start(speed)    
    GPIO.output(Input3, True)
    GPIO.output(Input4, False)
    GPIO.output(Input1, True)
    GPIO.output(Input2, False)
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

    
while True:
    try:
        s1= GPIO.input(max_left_sensor)
        s2= GPIO.input(left_sensor)
        s3= GPIO.input(center_sensor)
        s4= GPIO.input(right_sensor)
        s5= GPIO.input(max_right_sensor)
        
        forward(100);
        # UUTIEN1: max_left + max_right =0 --> stop
        if (s1 + s5 + s2 + s3 + s4) == 0:
            stop()
            break;
        # UUTIEN2: max_left --> hard left
        #          max_right --> hard right
        elif (s1+s2+s3) == 0:
            left(60)
#             only_right_wheel(50)
            sleep(0.02)
#             left(80)
#             while GPIO.input(center_sensor)!= 0:
#                 print("turning...")
        elif (s5+s4+s3) == 0:
            right(60)
#             only_left_wheel(50)
            sleep(0.02)
#             right(80)
#             while GPIO.input(center_sensor)!= 0:
#                 print("turning...")
        # UUTIEN3: left/right --> left/right
        elif (s2+s3) == 0:
            left(50)
#             only_right_wheel(50)
            sleep(0.02)
#             while GPIO.input(center_sensor)!= 0:
#                 print("turning...")
        elif (s4+s3) == 0:
            right(50)
#             only_left_wheel(50)
            sleep(0.02)
#             while GPIO.input(center_sensor)!= 0:
#                 print("turning...")
        # uutien4: center --> slow
        elif s5 == 0:
            right(60)
#             only_right_wheel(50)
            sleep(0.02)
        elif s1 == 0:
            left(60)
#             only_left_wheel(50)
            sleep(0.02)
        elif s4 == 0:
#             diff_wheel(20,70)
            right(40)
            sleep(0.02)
        elif s2 == 0:
#             diff_wheel(70,20)
            left(40)
            sleep(0.02)
        elif s3 == 1:
            forward(50)
#             sleep(0.02)
        else:
            forward(40)
#             sleep(0.02)
        print(str(s1)+" "+str(s2)+" "+str(s3)+" "+str(s4)+" "+str(s5))
        sleep(0.01)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
GPIO.cleanup()

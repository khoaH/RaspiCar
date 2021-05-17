import pigpio
from time import sleep

# connect to the 
pi = pigpio.pi()

# loop forever
def servoRotate(goc):
    pi.set_servo_pulsewidth(12, goc)    # off
    sleep(1)
    
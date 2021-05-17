import RPi.GPIO as IO  
from time import sleep 


servo=12
IO.setwarnings(False)  
IO.setmode (IO.BCM)   
IO.setup(servo,IO.OUT) 
p = IO.PWM(servo,50)   
p.start(0)             
def runServo(goc):
    try:
        Angle = goc
        if (Angle<=180) and (Angle>=0):       
                DutyCycle = Angle/18+2        
                p.ChangeDutyCycle(DutyCycle)
    except KeyboardInterrupt:
        IO.cleanup()


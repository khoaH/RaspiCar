import robot
import servoNJt as servo
import time
import threading
import ultrasonic_2 as usc
import RPi.GPIO as IO

#robot.forward(5)

#robot.right(5)

# robot.left(5)
global distance
global left
global right
def ultraSonicServo():
    while True:
        if usc.distanceReturn()<40:
            #stop()-
           robot.forward(0);
           servo.servoRotate(2500)
           time.sleep(1)
           left=usc.distanceReturn()
           print('left ' + str(left))
           time.sleep(0.5)
           servo.servoRotate(500)
           time.sleep(1)
           right=usc.distanceReturn()
           print('right ' + str(right))
           if left>right:
                servo.servoRotate(1500)
                robot.left(0.5)
                robot.forward(1.5)
                robot.right(0.3)
                robot.forward(2)
                
                #time.sleep(1)
           elif right>left:
                servo.servoRotate(1500)
                robot.right(0.5)
                #time.sleep(1)
                #robot.forward(5)
        else:
            servo.servoRotate(1500)
            robot.forward(1)
            


#threadServo=threading.Thread(target=servo.runServo,args=(90,))
#threadRobot=threading.Thread(target=robot.forward,args=(5,))
#threadServo.start()
#threadRobot.start()
#robot.forward(3);
ultraSonicServo()
#IO.cleanup()

# Auto.py file, part 2
while True:
    try:
        if GPIO.input(lf_l) == False and GPIO.input(lf_r) == True:
            right()
        elif GPIO.input(lf_r) == False and GPIO.input(lf_l) == True:
            Left()
        else:
            in front()
            sleep(0.01)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()

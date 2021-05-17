import time
import board
import adafruit_bh1750
from gpiozero import LED

 
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

light= LED(26)
 
while True:
    print("%.2f Lux" % sensor.lux)
    if sensor.lux < 10:
        light.on()
    else:
        light.off()
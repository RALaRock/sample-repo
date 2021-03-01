# learning to use GPIO

# import the GPIO and time packages
import RPI.GPIO as GPIO
import time

# set the pin configuration to BOARD
# pins numbered 1 2
#               3 4 and so on
GPIO.setmode(GPIO.BOARD)
# configure pin 7 as an output
GPIO.setup(7, GPIO.OUT)
# loop turning the pin on and off for 1 second
for i in range(50):
    GPIO.output(7, True)
    if GPIO
    time.sleep(1)
    GPIO.output(7, False)
    time.sleep(1)

GPIO.cleanup()

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
while True:
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(0.1)
     
    
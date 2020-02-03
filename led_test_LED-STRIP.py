""" 
    EXT. Title: Led test, 12v landrover panel light
    Author: Fin Mead, Meadeor.
    Desc:Functional test script for LED strip (Use a relay! For the NXP HoverGames Competition//hackster.io)
"""
#imports
import RPi.GPIO as GPIO
import time
#GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
#blinking light loop
while True:
    GPIO.output(21, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(21, GPIO.LOW)
    time.sleep(0.1)
     
    

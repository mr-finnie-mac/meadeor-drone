""" 
    EXT. Title: BUzzer test, beeping
    Author: Fin Mead, Meadeor.
    Desc:Functional test script for buzzer/siren (For the NXP HoverGames Competition//hackster.io)
"""
#imports
import RPi.GPIO as GPIO
import time

#GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

#beeping loop
while True:
    GPIO.output(24, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(24, GPIO.LOW)
    time.sleep(0.1)
#Use a buzzer and you can mimick a siren using GPIO.HIGH/LOW radpidly
    

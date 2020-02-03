""" 
    EXT. Title: Guidance & Alert programming test
    Author: Fin Mead, Meadeor.
    Desc: Allows access to light and audio hardware. Relay light panel and buzzer (For the NXP HoverGames Competition//hackster.io)
"""
#imports
import RPi.GPIO as GPIO
import time
#setting up GPIOs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)#LED strip
GPIO.setup(24, GPIO.OUT)#Buzzer/siren
#Repeating Ligh/buzzer alarm (flashing and beeping)
while True:
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    time.sleep(0.1)# change sleep parameter to make it faster or slower
    GPIO.output(21, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(0.1)# ~and here

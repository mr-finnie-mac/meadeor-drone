""" 
    EXT. Title: PixyCam2 Fire detection script for Raspberry Pi - posts to twitter and controls onboard drone light/speaker.
    Author: Fin Mead, Meadeor.
    Desc: Main script for Raspberry Pi fire detection/tweet/alert script (For the NXP HoverGames Competition//hackster.io)
"""
#Pixy imports
from __future__ import print_function
import pixy 
from ctypes import *
from pixy import *

#GPIO imports - alert hardware
import RPi.GPIO as GPIO
import time

#Twitter imports - twython
from twython import Twython

#Twitter imports - api auth. keys #Use your own keys and tokens!
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#GPIO light/sound setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)#red LED bar
GPIO.setup(24, GPIO.OUT)#siren buzzer

#drone - visual and audio alert procedure
def onboardAlert():
    i = 0
    for i in range(10):
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(0.2)
        i = i + 1

#Drone data
droneLoc = ("N'111 E'111") #! This is where I would have added in telemetry data if I had the Pi companion working properly. -See Story on hackster.io/meadeor

#Pixy2 Python SWIG Fire recognition/pixy module stuff - This is code I adapted from their demo scripts
print("Pixy2 Python SWIG Fire recognition and tweet")
pixy.init ()
pixy.change_prog ("color_connected_components");
#Building signature blocks...
class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]

blocks = BlockArray(100)
frame = 0

while 1:
  count = pixy.ccc_get_blocks (100, blocks)

  if count > 0:
    print('frame %3d:' % (frame))
    frame = frame + 1
    for index in range (0, count):
      print('[BLOCK: SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].m_signature, blocks[index].m_x, blocks[index].m_y, blocks[index].m_width, blocks[index].m_height))#PixyCam2 return statement from demo script
      
      #Twitter API handling/posting
      image = open('firreAlertSign.jpg', 'rb') #Fire alert image upload
      response = twitter.upload_media(media=image)
      media_id = [response['media_id']]
      message = "(test)Potential Fire at: " + droneLoc #tweet coordinates *Fake coordinates/alert for testing!
      twitter.update_status(status=message, media_ids=media_id)
      print("TWEETED: " + message)
      
      #Physical Drone Alert
      print("Onboard audio-visual alert system is active")
      onboardAlert() #alert triggered for 10 seconds only to avoid spamming.
   

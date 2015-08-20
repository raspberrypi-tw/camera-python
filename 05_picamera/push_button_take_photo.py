#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# push_button_take_photo.py
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO                 
import time
import picamera

GPIO.setmode(GPIO.BOARD)                
BTN_PIN = 11
GPIO.setup(BTN_PIN, GPIO.IN)

def callback_function(channel):                                                 
    print("Start to take a photo...")
    with picamera.PiCamera() as camera:
        # Camera warm-up time
        #time.sleep(2)
        # The default resolution is 1280x800
        camera.capture('image.jpg')
    print("End to take")

try:
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=callback_function, bouncetime=2000)

    while True:
        time.sleep(10)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          

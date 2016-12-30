#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2017, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Author : sosorry
# Date   : 11/14/2017
# Capture an image to a file

import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    # Camera warm-up time
    #time.sleep(2)
    # The default resolution is 1280x800
    camera.capture('image.jpg')

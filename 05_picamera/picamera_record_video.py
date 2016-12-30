#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2017, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# picamera_record_video
# Recording video to a file
#
# Author : sosorry
# Date   : 11/14/2017

import picamera

with picamera.PiCamera() as camera:
    camera.start_recording('video.h264')
    camera.wait_recording(3)
    camera.stop_recording()


#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Author : sosorry
# Date   : 05/31/2015
# Origin : https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md

使用：直接在終端機下指令

1. 錄5秒(-t) 1080p30影片(預設w/h = 1920/1080)
$ raspivid -t 5000 -o video.h264

2.錄5秒(-t) 1080p30影片, 影片存檔名稱video.h264(-o), bitrate為3.5MBits/s(-b)
$ raspivid -t 5000 -o video.h264 -b 3500000

3. 錄5秒(-t) 1080p30影片, 長640(-w) x 寬480(-h)
$ raspivid -t 5000 -w 640 -h 480



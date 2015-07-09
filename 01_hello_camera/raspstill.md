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
# Origin : https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md

使用：直接在終端機下指令

1. 只預覽2秒(-t), 不存檔
$ raspistill -t 2000

2. 5秒後拍照, 檔案test.jpg(-o), 印出詳細訊息(-v)
$ raspistill -v -o test.jpg 

3. 3秒後拍照, 並編碼成png格式(-e), 長640(-w) x 寬480(-h)
$ raspistill -t 3000 -o test.png -e png -w 640 -h 480


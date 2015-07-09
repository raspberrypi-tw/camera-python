#!/bin/bash

raspivid -o - -t 0 -w 320 -h 240 -n | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264


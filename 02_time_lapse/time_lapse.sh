#!/bin/bash

raspistill -t 60000 -tl 1000 -o image%04d.jpg -bm -w 640 -h 480
ls *.jpg > stills.txt
mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=4/3:vbitrate=8000000 -vf scale=640:480 -o timelapse.avi -mf type=jpeg:fps=4 mf://@stills.txt


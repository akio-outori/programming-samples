#!/usr/bin/python

# Python example script to force us to take a break and play a video

import time
import webbrowser

video = "https://www.youtube.com/watch?v=HBBb42hHyb0"
delay = "10"
break_count = 0
total_breaks = 3

def break_time(delay, video):
	webbrowser.open(video)
	time.sleep(float(delay))

while(break_count < total_breaks):
	break_time(delay, video)

#!/usr/bin/python
import pifacedigitalio
import subprocess
# from time import sleep

pfd = pifacedigitalio.PiFaceDigital()

pfd.leds[5].turn_on() #Room light ON

def toggle_led0(event):
	subprocess.call("./goshow.sh", shell=True)
	
pifacedigital = pifacedigitalio.PiFaceDigital()
listener = pifacedigitalio.InputEventListener(chip=pifacedigital)
listener.register(0, pifacedigitalio.IODIR_FALLING_EDGE, toggle_led0)
listener.activate()
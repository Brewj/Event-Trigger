#!/usr/bin/python
import pifacedigitalio
import os
from time import sleep
pfd = pifacedigitalio.PiFaceDigital()

pfd.leds[1].turn_on() #On Air and Cabinet ON
sleep (2) #Delay for lights
pfd.leds[0].turn_off() #Room light OFF
sleep (1)
os.system("aplay /home/pi/withy_edit.wav") #Audio GO
sleep (3) #End Delay
pfd.leds[0].turn_on() #Room light ON
sleep (1)
pfd.leds[1].turn_off() #On Air and Cabinet OFF

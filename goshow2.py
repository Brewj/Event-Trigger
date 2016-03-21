#!/usr/bin/python    
import pifacedigitalio    
import subprocess    
from time import sleep 
import os   
      
pfd = pifacedigitalio.PiFaceDigital() 
listener = pifacedigitalio.InputEventListener(chip=pfd)  

#Standby State
pfd.leds[0].turn_on() #Room light ON    
 
 #Go Show   
def toggle_led0(event):    
	listener.deactivate() #Inhibit button  
	pfd.leds[1].turn_on() #On Air and Cabinet ON, Video Go  
	sleep (2) #Delay for lights    
	pfd.leds[0].turn_off() #Room light OFF    
	sleep (1) #Delay before audio
	os.system("aplay /home/pi/wim.wav") #Audio GO    
	sleep (3) #End Delay    
	pfd.leds[0].turn_on() #Room light ON    
	sleep (1)    
	pfd.leds[1].turn_off() #On Air and Cabinet Off
	#listener.activate() #re arm button    
    
if __name__ == "__main__":    
	listener.register(0, pifacedigitalio.IODIR_FALLING_EDGE, toggle_led0)  
	listener.activate()    
  
  
while True:    
  pass   
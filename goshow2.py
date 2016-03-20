#!/usr/bin/python  
import pifacedigitalio  
import subprocess  
from time import sleep  
    
pfd = pifacedigitalio.PiFaceDigital()
pifacedigital = pifacedigitalio.PiFaceDigital() 
listener = pifacedigitalio.InputEventListener(chip=pifacedigital)
listener.register(0, pifacedigitalio.IODIR_FALLING_EDGE, toggle_led0)
listener.activate()     
    
pfd.leds[5].turn_on() #Room light ON  
  
def toggle_led0(event):  
	listener.deactivate() #Inhibit button
	pfd.leds[1].turn_on() #On Air and Cabinet ON  
	sleep (2) #Delay for lights  
	pfd.leds[0].turn_off() #Room light OFF  
	sleep (1)  
	os.system("aplay /home/pi/withy_edit.wav") #Audio GO  
	sleep (3) #End Delay  
	pfd.leds[0].turn_on() #Room light ON  
	sleep (1)  
	pfd.leds[1].turn_off()   
	listener.activate() #re arm button  
  
if __name__ == "__main__":  
    
  while True:  
  	pass  



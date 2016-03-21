# Event-Trigger
PiFace Digital Event trigger
21st March 2016
I have now combined the program into a single file, goshow2.py  I'm still trying to get the listener.deactivate function to work however, it is not.

This is the error I'm getting
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 810, in __bootstrap_inner
    self.run()
  File "/usr/lib/python2.7/threading.py", line 763, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/usr/lib/python2.7/dist-packages/pifacecommon/interrupts.py", line 341, in handle_events
    function(event)
  File "goshow2.py", line 15, in toggle_led0
    listener.deactivate() #Inhibit button
  File "/usr/lib/python2.7/dist-packages/pifacecommon/interrupts.py", line 222, in deactivate
    self.dispatcher.join()
  File "/usr/lib/python2.7/threading.py", line 940, in join
    raise RuntimeError("cannot join current thread")
RuntimeError: cannot join current thread

14th March 2016
I have two files, standby.py run from standby.sh this is listening to the input of sw1 on the PiFace
When triggered goshow.py runs a series of events.

I'm trying dissable sw1 when goshow is active anyone any ideas?

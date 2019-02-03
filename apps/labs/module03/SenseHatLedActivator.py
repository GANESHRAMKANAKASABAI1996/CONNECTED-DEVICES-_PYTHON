'''
Created on Feb 1, 2019
@author: GANESHRAM KANAKASABAI
'''
from time import sleep#importing sleep to set delay
from sense_hat import SenseHat#importing SenseHat module to control Raspberry pi SenseHAT
import threading#importing threading module to construct threading interfaces
'''
Creating class SenseHatLedActivator which sets the LED value to low and sets the display parameters
'''
class SenseHatLedActivator(threading.Thread):
    enableLed = False
    rateInSec = 1
    rotateDeg = 270
    sh = None
    displayMsg = None
    
    def __init__(self, rotateDeg = 270, rateInSec = 1):#parameterized constructor
        super(SenseHatLedActivator, self).__init__()# _init_() is called during object initialization.
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
        self.sh = SenseHat()
        self.sh.set_rotation(self.rotateDeg)
        
    def run(self):#overriding run method is used to perform the desired functionality
        while True:
            if self.enableLed:
                if self.displayMsg != None:
                    #print(self.displayMsg);
                    self.sh.show_message(str(self.displayMsg))
                else:
                    print('R')
                    self.sh.show_letter(str('R'))
                sleep(self.rateInSec)
                self.sh.clear()
                sleep(self.rateInSec)
                
    def getRateInSeconds(self):#returns the rate of display in seconds
        return self.rateInSec
    
    def setEnableLedFlag(self, enable):#sets the flag value to high
        self.enableLed = True;
        
    def setDisplayMessage(self, msg):#displays the message in the sense HAT
        self.displayMsg = msg
'''
Created on Feb 1, 2019
@author: GANESHRAM KANAKASABAI
'''
from labs.common import ActuatorData
from labs.module03 import SenseHatLedActivator

class TempActuatorEmulator():#Creating a class TempActuatorEmulator
    '''
    classdocs
    '''
        
    def __init__(self):
        '''
         _init_() is called during object initialization.
        '''
        self.actuator_data = ActuatorData.ActuatorData();
          
    def publishMessage(self,act_data):
        if act_data!=self.actuator_data:
            self.val = act_data.getValue();
        
            if act_data.getCommand()==2:
                mes = "Decrease the Temperature by %.2f" %(self.val);
            else:
                mes = "Increase the Temperature by %.2f" %(self.val);
                print("______________________________________________");
            sense_hat = SenseHatLedActivator.SenseHatLedActivator();
            sense_hat.setDisplayMessage(mes);
            sense_hat.setEnableLedFlag('enable');#triggers the start of sense_hat
        
            try:
                sense_hat.start();#starts the execution of the sense_hat 
            except:
                print("Couldn't activate Actuator !!!!!");
            finally:
                sense_hat.enableLed = False
                self.actuator_data.updateData(act_data);
        
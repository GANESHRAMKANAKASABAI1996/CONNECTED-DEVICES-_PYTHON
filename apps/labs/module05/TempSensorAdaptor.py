'''
Created on Jan 24, 2019
@author: GANESHRAM KANAKASABAI
'''

from threading import Thread # importing thread 
from random import uniform # importing uniform function to create random float numbers
from labs.common import SensorData # importing SensorData class to use the attributes of sensor
from time import sleep # importing sleep to set delay
from datetime import datetime
from labs.common.DataUtil import DataUtil#importing DataUtil
import json

from labs.module02 import SmtpClientConnector # importing SmtpClientConnector to email the notification

from labbenchstudios.common import ConfigUtil 

from labs.common import ActuatorData#importing ActuatorData
from labs.module03 import TempActuatorEmulator#importing TempActuatorEmulator
'''
Creating a class TempSensorAdaptor so that the generated sensorData could be sent
as JSON to our email address and the generated sensorData content could be written
as JSON into the filesystem

'''
class TempSensorAdaptor(Thread):
    '''
    constructor
    @param name:returns object with the given name
    '''
    def __init__(self, name):
        '''
    Constructor
    Creates object of SensorData, ConfiUtil and TempActuatorEmulator
    This class is used to send notification through mail 
    and initiate an action to control the temperature 
        '''
        Thread.__init__(self);
        self.enableEmulator = True; # flag to enable emulator function
        self.sensor = SensorData.SensorData(name, 0, 30); # creating a sensor data object
        self.temp = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props'); 
        self.temp_emul = TempActuatorEmulator.TempActuatorEmulator();
        
        '''
        This function is used to store the json formatted data to a text file 
        @param value : The value indicates the data 
        @param filename : The filename indicates the filename to which json data is to be stored
        '''
    def fileWrite(self,value,filename):
        with open(filename,'w'):
            json.dumps(value)
        
        '''
        This thread gets the current temperature from SenseHat. 
        if the current value is greater than given threshold notification is generated and email
        If the current temperature is not equal to nominal temperature, signal is sent to actuator 
        to revert it back to normal
        '''
              
    def run(self):
        while True:
            if self.enableEmulator:
                self.sensor.curVal = uniform(float(self.sensor.getMinValue()), float(self.sensor.getMaxValue())); 
                self.sensor.addValue(self.sensor.curVal);
                self.sensor.diffVal = self.sensor.curVal - self.sensor.avgVal;
                print(self.sensor);
                if self.sensor.curVal >= (self.sensor.getAvgValue() + 2):
                    data = DataUtil()
                    self.sensor.timestamp = datetime.now();
                    json_data = data.toJsonfromSensor(self.sensor);
                    SensorData.SensorData.breach_values.append(self.sensor);
                    print(SensorData.SensorData.breach_values)
                    print("warning!!Temperature exceeded the average temperature by %.2f degrees" %(self.sensor.diffVal));
                    sen_not = SmtpClientConnector.SmtpClientConnector(); 
                    sen_not.publishMessage("Temperature Notification", json_data); 

                sleep(3);#sleep function delays the time of execution by 3 seconds
                
                
    
            
        
        
        
        
        
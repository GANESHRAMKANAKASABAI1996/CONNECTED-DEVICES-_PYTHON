'''
Created on Jan 24, 2019
@author: GANESHRAM KANAKASABAI
'''

from threading import Thread # importing thread 
from random import uniform # importing uniform function to create random float numbers
from labs.common import SensorData # importing SensorData class to use the attributes of sensor
from time import sleep # importing sleep to set delay
from labs.module02 import SmtpClientConnector # importing SmtpClientConnector to email the notification
from labs.common import ConfigUtil 
from labs.common import ConfigConst 
from datetime import datetime #importing datetime to manipulate with date and time values
from labs.common import ActuatorData
from labs.module03 import TempActuatorEmulator

class TempSensorAdaptor(Thread):
    '''
    classdocs
    '''

    def __init__(self, name):
        '''
         _init_() is called during object initialization.
        '''
        Thread.__init__(self);
        self.enableEmulator = True; # flag to enable emulator function
        self.sensor = SensorData.SensorData(name, 0, 30); # creating a sensor data object
        self.temp = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props'); 
        self.temp_emul = TempActuatorEmulator.TempActuatorEmulator();
        '''
        This thread generates a random float variable(Current Value). 
        if the current value is greater than given threshold notification is generated
        '''
    def run(self):#overriding run method is used to perform the desired functionality
        while True:
            if self.enableEmulator:
                #sense = SenseHat();
                #self.sensor.curVal = sense.get_temperature_from_pressure();
                self.sensor.curVal = uniform(float(self.sensor.getMinValue()), float(self.sensor.getMaxValue())); 
                self.sensor.addValue(self.sensor.curVal);
                nominal_temp = self.temp.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.NOMINAL_TEMP)
                self.sensor.diffVal = self.sensor.curVal - self.sensor.avgVal;
                print(self.sensor);
                if self.sensor.curVal >= (self.sensor.getAvgValue() + 2):
                    data = (self.sensor);
                    self.sensor.timestamp = datetime.now();
                    SensorData.SensorData.breach_values.append(self.sensor);
                    print(SensorData.SensorData.breach_values)
                    print("Warning!! value of temperature exceeded the average temperature by %.2f degrees" %(self.sensor.diffVal));
                    sen_not = SmtpClientConnector.SmtpClientConnector(); 
                    sen_not.publishMessage("Temperature Notification", data); 
                if self.sensor.curVal!=nominal_temp:
                    self.actuator_data = ActuatorData.ActuatorData();
                    self.diff = (self.sensor.curVal - float(nominal_temp));
                    if self.diff>0:
                        self.actuator_data.setValue(self.sensor.curVal - float(nominal_temp))
                        self.actuator_data.setCommand(ActuatorData.COMMAND_SET);
                    else:
                        self.actuator_data.setValue(float(nominal_temp) - self.sensor.curVal)
                        self.actuator_data.setCommand(ActuatorData.COMMAND_RESET);
                    print("Actual Vale : ",str(self.actuator_data.getValue()));
                    self.temp_emul.publishMessage(self.actuator_data)
                delay = int(self.temp.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.POLL_CYCLES_KEY));     
                sleep(delay);
                
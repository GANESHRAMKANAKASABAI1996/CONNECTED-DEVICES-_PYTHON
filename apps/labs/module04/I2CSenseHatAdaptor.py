'''
Created on Feb 8, 2019

@author: GANESHRAM KANAKASABAI
'''

import smbus#Allows SMBus access through I2C interface
import threading#importing threading module to construct threading interfaces
from time import sleep#importing sleep to set delay
from labs.common import ConfigUtil#importing ConfigUtil
from labs.common import ConfigConst#importing ConfigConst

i2cBus = smbus.SMBus(1) # Use I2C bus No.1 on Raspberry Pi3 +
enableControl = 0x2D
enableMeasure = 0x08
accelAddr = 0x1C # address for IMU (accelerometer)
magAddr = 0x6A # address for IMU (magnetometer)
pressAddr = 0x5C # address for pressure sensor
humidAddr = 0x5F # address for humidity sensor
begAddr = 0x28
totBytes = 6
DEFAULT_RATE_IN_SEC = 5

'''
Class I2CSenseHatAdaptor is used to capture all the data from the accelerometer,
magnetometer, pressure and humidity sensors by passing the thread arguments
as parameters.
'''
class I2CSenseHatAdaptor(threading.Thread):
    rateInSec = DEFAULT_RATE_IN_SEC
   
    '''
    def_init_(self) is a constructor which is used to send data to the sensehat module.
    _init_() is called during object initialization.
    '''
    def __init__(self):
        super(I2CSenseHatAdaptor, self).__init__()
        self.config = ConfigUtil.ConfigUtil(ConfigConst.ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        self.initI2CBus()
        
    '''
    The function initI2CBus(self) is used for initializing the I2C bus 
    and enabling the I2C address.
    WriteQuick method is used to send a single bit to the device in place 
    of Rd/Wr bit. 
    '''    
    def initI2CBus(self):
        print("Initializing I2C bus and enabling I2C addresses...")
        
        i2cBus.write_quick(accelAddr)
        i2cBus.write_quick(magAddr)
        i2cBus.write_quick(pressAddr)
        i2cBus.write_quick(humidAddr)
        
    '''
    Overriding run method from the Thread class to attain desired functionality
    This Thread will display the sensor data for fixed amount of time and can be 
    varied using the variable rateInSec.
    '''    
    def run(self):
        while True:
            if self.enableEmulator:
                
                self.displayAccelerometerData()
                self.displayMagnetometerData()
                self.displayPressureData()
                self.displayHumidityData()
            sleep(self.rateInSec)
    
    '''
    Function to read accelerometer data that can sense either static or dynamic forces of 
    acceleration and display the output in human readable format.
    '''     
    def displayAccelerometerData(self):
        self.accl_data = i2cBus.read_i2c_block_data(0x1C, begAddr, 1)#Block Read Transaction
        print("Accelerometer"+ str(self.accl_data));
    
    '''
    Function to read magnetometer data that detects the strength and direction of the local
    magnetic field and display the output in human readable format.
    '''      
    def displayMagnetometerData(self):
        self.mag_data = i2cBus.read_i2c_block_data(0x6A, begAddr, 1)#Block Read Transaction
        print("Magnetometer"+ str(self.mag_data));
    
    '''
    Function to read pressure data from the Sensehat that basically acts as a pressure
    transducer and display the output in human readable format.
    '''        
    def displayPressureData(self):
        self.pres_data = i2cBus.read_i2c_block_data(0x5C, begAddr, 1)#Block Read Transaction
        print("Pressure"+ str(self.pres_data));
    
    '''
    Function to read humidity data that gets the percentage of relative humidity from the
    humidity sensor and display the output in human readable format.
    '''    
    def displayHumidityData(self):
        self.humid_data = i2cBus.read_i2c_block_data(0x5F, begAddr, 1)#Block Read Transaction
        print("Humidity"+ str(self.humid_data));
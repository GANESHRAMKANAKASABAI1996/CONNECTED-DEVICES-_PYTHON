'''
Created on Jan 24, 2019
@author: GANESHRAM KANAKASABAI
'''

from time import sleep  # importing sleep function to set delay
from labs.module03.TempSensorAdaptor import TempSensorAdaptor  # importing TempSensorEmulator Class to measure temperature
'''
 Creating a new object to measure temperature and monitor
'''
sensor_data = TempSensorAdaptor("Temperature Data");  
'''
When the program quits,any daemon threads are killed automatically
'''
sensor_data.daemon = True;
sensor_data.start();#starting the activity of thread

while True:
    sleep(1);# The sleep() suspends the execution for the fixed number of seconds.
    pass
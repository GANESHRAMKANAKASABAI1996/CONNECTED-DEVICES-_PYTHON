'''
Created on Jan 24, 2019
@author: GANESHRAM KANAKASABAI
'''

from time import sleep  # importing sleep function to set delay
from labs.module05.TempSensorAdaptor import TempSensorAdaptor  

'''
 Creating a new object to measure temperature and monitor
 When the program quits,any daemon threads are killed automatically
 sensor_data.start() starts the activity of the thread
'''

sensor_data = TempSensorAdaptor("Temperature Data");  
sensor_data.daemon = True;
sensor_data.start();

while True:
    sleep(3);# The sleep() suspends the execution for the fixed number of seconds.
    pass
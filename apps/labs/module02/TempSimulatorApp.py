'''
Created on Jan 24, 2019

@author: GANESHRAM KANAKASABAI
'''

from time import sleep #importing sleep function to set delay
'''
#importing SystemPerformanceAdaptor Class to measure system performance value
'''
from labs.module02 import TempSensorEmulator 
'''
# Creating a new thread to measure system performance 
'''
sensor_data = TempSensorEmulator.TempSensorEmulator("Temperature Data");  
sensor_data.start();#Starting the activity of thread

while True:
    sleep(1);#Pausing the execution of program for 1 second
    pass#Pass keyword here is used as a placeholder
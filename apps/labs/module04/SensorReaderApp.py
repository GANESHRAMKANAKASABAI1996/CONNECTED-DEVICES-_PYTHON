'''
Created on Jan 24, 2019
@author: GANESHRAM KANAKASABAI
'''
from time import sleep #importing sleep to set delay
from labs.module04 import I2CSenseHatAdaptor

'''
In this API instance of TempSensorEmulator is initialized
Derived Thread is made as Daemon thread
and calls start method to run.
# sensor_data.start() starts the activity of the thread.
'''
sensor_data = I2CSenseHatAdaptor.I2CSenseHatAdaptor()
sensor_data.daemon = True
sensor_data.start()

'''
Open an Infinite loop for this app to keep running
'''
while True:
    sleep(3)# The sleep(1) suspends the execution for 3 seconds.
    pass
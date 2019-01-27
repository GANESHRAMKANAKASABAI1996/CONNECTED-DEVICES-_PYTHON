'''
Created on Jan 24, 2019

@author: GANESHRAM KANAKASABAI
'''

from datetime import datetime#importing datetime for manipulating date and time
import os#importing the OS module  for using operating system dependent functionality
'''
Creating a class sensorData
'''

class SensorData(object):
    
    timestamp = None
    name = 'not set'
    curVal = 0;
    avgVal = 0;
    minVal = 0;
    maxVal = 30;
    totVal = 0;
    sampleCount = 0;
    
    def __init__(self, name,minVal,maxVal):
        '''
         Constructor to create object of SensorData Class
   
        @param name: Sensor name
        @param minVal: Minimum allowed value of the sensor
        @param maxVal: Maximum allowed value of the sensor  
        '''
        self.timestamp = str(datetime.now());
        self.name = name;
        self.maxVal = maxVal;
        self.minVal = minVal;
        '''
        addValue function adds and updates values of the previous total and calculates the average
        '''
        
    def addValue(self,newVal):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.curVal = newVal
        self.totVal += newVal
        if (self.curVal < self.minVal):
            self.minVal = self.curVal
        if (self.curVal > self.maxVal):
            self.maxVal = self.curVal
        if (self.totVal != 0 and self.sampleCount > 0):
            self.avgVal = self.totVal / self.sampleCount

    def getAvgValue(self):#getAvgValue function returns the average value
        return self.avgVal
    
    def getMaxValue(self):#getMaxValue function returns the maximum value
        return self.maxVal
    
    def getMinValue(self):#getMinValue function returns the minimum value
        return self.minVal
    
    def getValue(self):#getValue function returns the current value
        return self.curVal
    
        
    def __str__(self):#ToString method is used to obtain the string representation of the cell text
        self.customStr = \
        str(self.name + ':' + \
        os.linesep + '\tTime: ' + self.timeStamp + \
        os.linesep + '\tCurrent: ' + str(self.curVal) + \
        os.linesep + '\tAverage: ' + str(self.avgVal) + \
        os.linesep + '\tSamples: ' + str(self.sampleCount) + \
        os.linesep + '\tMin: ' + str(self.minVal) + \
        os.linesep + '\tMax: ' + str(self.maxVal))
        return self.customStr
'''
Created on Feb 1, 2019
@author: GANESHRAM KANAKASABAI
'''


import os #importing os
from datetime import datetime #importing datetime to perform date and time operations
COMMAND_OFF = 0
COMMAND_ON = 1
COMMAND_SET = 2
COMMAND_RESET = 3
STATUS_IDLE = 0
STATUS_ACTIVE = 1
ERROR_OK = 0
ERROR_COMMAND_FAILED = 1
ERROR_NON_RESPONSIBLE = -1
class ActuatorData():
    '''
    This class is created to create an Actuator Data to interact with Raspberry Pi
    '''
    
    def __init__(self):
        self.updateTimeStamp()
        
    timeStamp = None
    name = 'Not set'
    hasError = False
    command = 0
    errCode = 0
    statusCode = 0
    stateData = None
    val = 0.0
    
    '''
    This function returns the value of command
    
    '''
    def getCommand(self):
        return self.command
    
    '''
    This function returns the name
    @return: name
    
    '''    
    
    def getName(self):
        return self.name
    '''
    This function returns the state of the data
    @return: StateData
    '''
    
    def getStateData(self):
        return self.stateData
    '''
    This function is used to get status code
    @return: StatusCode
    '''
    
    def getStatusCode(self):
        return self.statusCode
    '''
    This function is used to get error code if present
    @return: errorCode
    '''
    
    def getErrorCode(self):
        return self.errCode
    '''
    This function is used to get the current value
    @return: value
    '''

    def getValue(self):
        return self.val;
    '''
    This function returns the error values
    @return: hasError
    '''
    def hasError(self):
        return self.hasError
    '''
    This function sets the command
    '''
    
    def setCommand(self, command):
        self.command = command
    '''
    This function is used to store name
    '''
    
    def setName(self, name):
        self.name = name
    '''
    This function stores the state data information
    '''
    
    def setStateData(self, stateData):
        self.stateData = stateData
    '''
    This function is used to store status code values
    '''
    
    def setStatusCode(self, statusCode):
        self.statusCode = statusCode
        
    '''
    Function is used to set error code
    @param errCode: Error Code 
    '''
    
    def setErrorCode(self, errCode):
        self.errCode = errCode
        if (self.errCode != 0):
            self.hasError = True
        else:
            self.hasError = False
            
    '''
    Function is used as a setter to set values in Actuator Data
    @param val: The difference between current temp and nominal temp 
    '''
    
    def setValue(self, val):
        self.val = val
        
    '''
    Updates the object with updated values
    @param data: updated values of Actuator Data 
    '''
    def updateData(self, data):
        self.command = data.getCommand()
        self.statusCode = data.getStatusCode()
        self.errCode = data.getErrorCode()
        self.stateData = data.getStateData()
        self.val = data.getValue()
    def updateTimeStamp(self):
        self.timeStamp = str(datetime.now())
        
    '''
    Its a toString function which presents object in human readable format
    @return: customStr : Object in human readable format
    '''
    def __str__(self):
        customStr = \
        str(self.name + ':' + \
        os.linesep + '\tTime: ' + self.timeStamp + \
        os.linesep + '\tCommand: ' + str(self.command) + \
        os.linesep + '\tStatus Code: ' + str(self.statusCode) + \
        os.linesep + '\tError Code: ' + str(self.errCode) + \
        os.linesep + '\tState Data: ' + str(self.stateData) + \
        os.linesep + '\tValue: ' + str(self.val))
        return customStr
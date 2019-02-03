'''
Created on Feb 1, 2019
@author: GANESHRAM KANAKASABAI
'''
import os#importing the OS module  for using operating system dependent functionality
from datetime import datetime#importing datetime to manipulate with date and time values
COMMAND_OFF = 0
COMMAND_ON = 1
COMMAND_SET = 2
COMMAND_RESET = 3
STATUS_IDLE = 0
STATUS_ACTIVE = 1
ERROR_OK = 0
ERROR_COMMAND_FAILED = 1
ERROR_NON_RESPONSIBLE = -1

class ActuatorData():#Creating class actuator data which would be responsible for sense_hat display
    '''
    constructor
     _init_() is called during object initialization.
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
    
    def getCommand(self):#returns commands
        return self.command
    
    def getName(self):#returns the name
        return self.name
    
    def getStateData(self):#returns the state data
        return self.stateData
    
    def getStatusCode(self):#returns status code
        return self.statusCode
    
    def getErrorCode(self):#returns error code
        return self.errCode
    
    def getValue(self):#returns the current value
        return self.val;
    
    def hasError(self):#returns the error value
        return self.hasError
    
    def setCommand(self, command):#stores command
        self.command = command
        
    def setName(self, name):#stores name
        self.name = name
        
    def setStateData(self, stateData):#stores state data
        self.stateData = stateData
        
    def setStatusCode(self, statusCode):#stores status code
        self.statusCode = statusCode
        
    def setErrorCode(self, errCode):#stores error code
        self.errCode = errCode
        if (self.errCode != 0):
            self.hasError = True
        else:
            self.hasError = False
            
    def setValue(self, val):#stores value
        self.val = val
        
    def updateData(self, data):#passes the data to corresponding containers
        self.command = data.getCommand()
        self.statusCode = data.getStatusCode()
        self.errCode = data.getErrorCode()
        self.stateData = data.getStateData()
        self.val = data.getValue()
        
    def updateTimeStamp(self):#stores the current time
        self.timeStamp = str(datetime.now())
    '''
    ToString function returns object in human readable format
    @return: Object in human readable customized format
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
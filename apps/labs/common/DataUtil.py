'''
Created on Feb 16, 2019

@author: GANESHRAM KANAKASABAI
'''

import json
from labs.common.SensorData import SensorData
from labs.common.ActuatorData import ActuatorData

class DataUtil(object):
    '''
    This class contains function for conversion from 
    json to Sensor Data object and vice versa
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    '''
    Function to convert SensorData to json data
    @param SensorData : SensorData object
    @return jsonSd : Json data
    '''
    def toJsonfromSensor(self, SensorData):
        data = {};
        data['name'] = SensorData.name;
        data['avgVal'] = SensorData.avgVal;
        data['maxVal'] = SensorData.getMaxValue();
        data['minVal'] = SensorData.getMinValue();
        data['curVal'] = SensorData.getValue();
        data['timeStamp'] = str(SensorData.timestamp);
        self.jsonSd = json.dumps(data)
        outputSd = open('sensordata.txt','w')
        outputSd.write(self.jsonSd)
        return self.jsonSd
    
    '''
    Function to convert SensorData to json data
    @param SensorData : SensorData object
    @return jsonSd : Json data
    '''    
    def toSensorfromJson(self,jsonData):
        sdDict = json.loads(jsonData)
        
        sd = SensorData('Temperature',0,30)
        sd.name = sdDict['name']
        sd.timeStamp = sdDict['timeStamp']
        sd.avgVal = sdDict['avgVal']
        sd.minVal = sdDict['minVal']
        sd.maxVal = sdDict['maxVal']
        sd.curVal = sdDict['curVal']
        
        return sd
    '''
    Function to convert Json to Actuator data
    @param actuatordata : ActuatorData object
    @return jsonSd : Json data
    ''' 
    def actuatorTojson(self,actuatordata):
        self.jsonAd = json.dumps(actuatordata.__dict__)
        outputAd = open('actuatordata.txt','w')
        outputAd.write(self.jsonAd)
        return self.jsonAd
     
    '''
    Function to convert ActuatorData to json data
    @param jsondata : JsonData object
    @return ad : ActuatorData data
    '''
    def jsonToactuator(self,jsonData):
        adDict = json.loads(jsonData)
        ad = ActuatorData()
        ad.name = adDict['name']
        ad.timeStamp = adDict['timeStamp']
        ad.hasError = adDict['hasError']
        ad.command = adDict['command']
        ad.errCode = adDict['errCode']
        ad.statusCode = adDict['statusCode']
        ad.stateData = adDict['stateData']
        ad.curValue = adDict['curValue']  
        return ad
        
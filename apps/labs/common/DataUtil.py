'''
Created on Feb 16, 2019

@author: GANESHRAM KANAKASABAI
'''

import json#importing json
from labs.common.SensorData import SensorData#importing sensorData
from labs.common.ActuatorData import ActuatorData#importing ActuatorData
'''
Creating a class DataUtil where the data is transformed to json format 
which is been stored as a text file
'''
class DataUtil(object):
    '''
    constructor
    _init_() is called during object initialization.
    '''
    
    def __init__(self):
        '''
     Function toJsonfromSensor is used to transform the data from the sensor to
     json format
     @param sensor data : The sensor data is transformed into json format
        '''
    
    def toJsonfromSensor(self, SensorData):
        data = {};
        data['name'] = SensorData.name;
        data['avgVal'] = SensorData.avgVal;
        data['maxVal'] = SensorData.getMaxValue();
        data['minVal'] = SensorData.getMinValue();
        data['curVal'] = SensorData.getValue();
        data['time'] = str(SensorData.timestamp);
        self.jsonSd = json.dumps(data)
        outputSd = open('sensordata.txt','w')
        outputSd.write(self.jsonSd)
        return self.jsonSd
    '''
    Function toSensorfromJson is used to transform the Json data to sensor readable data
    @param json data : json data is transformed to sensor readable data
    '''
        
    def toSensorfromJson(self,jsonData):
        sdDict = json.loads(jsonData)
        #print(" decode [pre] --> " + str(sdDict))
        sd = SensorData()
        sd.name = sdDict['name']
        sd.timeStamp = sdDict['timeStamp']
        sd.avgValue = sdDict['avgValue']
        sd.minValue = sdDict['minValue']
        sd.maxValue = sdDict['maxValue']
        sd.curValue = sdDict['curValue']
        sd.totValue = sdDict['totValue']
        sd.sampleCount = sdDict['sampleCount']
        #print(" decode [post] --> " + str(sd))
        return sd
    '''
    This function is used to transform the actuator data into json format
    @param actuator data : this actuator data is transformed to json
    '''
    
    def actuatorTojson(self,actuatordata):
        self.jsonAd = json.dumps(actuatordata.__dict__)
        outputAd = open('actuatordata.txt','w')
        outputAd.write(self.jsonAd)
        return self.jsonAd
    '''
    This function is used to transform the json formatted data into actuator data
    @param jsonData : This json data is transformed into actuator data 
    '''
    
    def jsonToactuator(self,jsonData):
        adDict = json.loads(jsonData)
        #print(" decode [pre] --> " + str(adDict))
        ad = ActuatorData()
        ad.name = adDict['name']
        ad.timeStamp = adDict['timeStamp']
        ad.hasError = adDict['hasError']
        ad.command = adDict['command']
        ad.errCode = adDict['errCode']
        ad.statusCode = adDict['statusCode']
        ad.stateData = adDict['stateData']
        ad.curValue = adDict['curValue']
        #print(" decode [post] --> " + str(ad))
        return ad
        
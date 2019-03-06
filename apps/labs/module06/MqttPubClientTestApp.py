'''
Created on Mar 5, 2019

@author: GANESHRAM KANAKASABAI
'''

from labs.common import ConfigConst
from labs.common.ConfigUtil import ConfigUtil
from labs.module06.MqttClientConnector import MqttClientConnector
'''
# importing SensorData class to use the attributes of sensor
'''
from labs.common.SensorData import SensorData 
from labs.common.DataUtil import DataUtil # importing DataUtil
import logging

from random import uniform
from datetime import datetime #importing datetime to perform date and time operations

topic = "Temperature Sensor"

config = ConfigUtil('../../../config/ConnectedDevicesConfig.props');
host = config.getProperty(ConfigConst.ConfigConst.MQTT_CLOUD_SECTION, ConfigConst.ConfigConst.HOST_KEY)

'''
Creating Sensor Data
'''
sensor = SensorData(topic,15,30)
sensor.curVal = uniform(float(sensor.getMinValue()), float(sensor.getMaxValue())); 
sensor.addValue(sensor.curVal);
sensor.diffVal = sensor.curVal - sensor.avgVal;
sensor.timestamp = datetime.now();
logging.info('SensorData to be sent:')
print("Sensor Value before converting to Json: "+str(sensor));

'''
Converting SensorData to json format
'''
data = DataUtil()
json_data = data.toJsonfromSensor(sensor);
logging.info('SensorData converted into Json:')
print("SensorData in Json Format before publishing"+str(json_data)+"\n")

pub_client = MqttClientConnector();

'''
Function is used to publish the Json to the MQTT broker through MQTT ClientConnector
@param topic:Topic of message
@param json_data: Json Payload
@param host: address of MQTT broker 
'''
pub_client.publish(topic,json_data,host)

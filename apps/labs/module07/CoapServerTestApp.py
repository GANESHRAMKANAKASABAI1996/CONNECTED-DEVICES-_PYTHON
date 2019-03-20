'''
Created on Mar 19, 2019

@author: GANESHRAM KANAKSABAI
'''

from labs.module07.CoapServerConnector import CoapServerConnector# importing CoapServerConnector

from labbenchstudios.common.ConfigUtil import ConfigUtil# importing ConfigUtil
from labbenchstudios.common import ConfigConst# importing ConfigConst

config = ConfigUtil('../data/ConnectedDevicesConfig.props')
config.loadConfig()

host = config.getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.HOST_KEY)
port = int(config.getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.PORT_KEY))

server = CoapServerConnector(host,port,config)

server.start()# starting the action of the server
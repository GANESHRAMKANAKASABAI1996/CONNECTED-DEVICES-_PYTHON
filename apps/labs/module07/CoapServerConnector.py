'''
Created on Mar 19, 2019

@author: GANESHRAM KANAKASABAI
'''
import getopt    
import sys
from coapthon.server.coap import CoAP 
from coapthon.server.coap import CoAP
from labs.module07.TempResourceHandler import TempResourceHandler 
from coapthon.resources.resource import Resource

from labbenchstudios.common.ConfigUtil import ConfigUtil
from labbenchstudios.common import ConfigConst

client = None

class CoapServerConnector(CoAP):
   

    def __init__(self,host,port,config):
        '''
        Constructor
        '''
        CoAP.__init__(self, (host, port))
        self.add_resource("temperature/", TempResourceHandler(config = config)) #Add Temperature resource while initializing server
        
    '''
    start function is used to start the server action
    '''
    def start(self):
        try:
            print("Starting Server...")
            self.listen(10)
        except KeyboardInterrupt:
            print("Server Shutdown")
            self.close()
            print("Exiting...")
        finally:
            self.close()
            
        

        
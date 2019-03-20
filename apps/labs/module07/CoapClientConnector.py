'''
Created on Mar 19, 2019

@author: GANESHRAM KANAKASABAI
'''
from coapthon.client.helperclient import HelperClient 
from coapthon.messages import request 

class CoapClientConnector():
    '''
    This is a helper class that connects to the CoAP server
    
    Attributes:
        host (str) - IP address of the server
        port (int) - Port number to connect to
        path (str) - Resource URI
    '''
    
    def __init__(self, host, port, path):
        self.host = host
        self.port = port
        self.path = path
        self.client = HelperClient(server=(host, port))
        
    
    def ping(self):
        '''
        Wrapper method to ping the server
        '''
            
        self.client.send_empty("")
        
    def get(self):
        '''
        Wrapper method for the GET action
        '''
        
        response = self.client.get(self.path)
        print(response.pretty_print())
    
    def post(self,jsonData):
        '''
        Wrapper method for the POST action
        
        Parameters:
            jsonData (str) - Request payload in JSON format
        '''
        
        response  = self.client.post(self.path, jsonData)
        print(response.pretty_print())
    
    def put(self, jsonData):
        '''
        Wrapper method for the PUT action
        
        Parameters:
            jsonData (str) - Request payload in JSON format
        '''
        
        response = self.client.put(self.path, jsonData)
        print(response.pretty_print())
        
    def delete(self):
        '''
        Wrapper method for the DELETE action
        '''
            
        response = self.client.delete(self.path)
        print(response.pretty_print())
        
    def stop(self):
        '''
        This method stops the client thread
        '''
        
        self.client.stop()     

        
        
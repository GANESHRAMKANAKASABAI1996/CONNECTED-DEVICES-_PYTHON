'''
Created on Jan 18, 2019

@author: GANESHRAM KANAKASABAI


'''
import psutil
from threading import Thread
from time import sleep
import datetime



class SystemPerformanceAdaptor(Thread):
    
    '''
    Class SystemPerformanceAdaptor extends the Thread class .
    '''


    def __init__(self,name,delay):
        Thread.__init__(self);
        self.name=name;
        self.delay=delay;
        
        self.en_thread=False;
        
        
        '''
        Constructor
        _init_() is called during object initialization.
          Thread._init_(self) method calls the parent _init_() method.
          Here, the en_thread flag is set to False
        '''
    def run(self):
        while self.en_thread:
            print("---------------------------------");
            print("New System Performance Settings\n")
            print("........printing the cpu stats.......");
            print(psutil.cpu_stats(),"\n");
            #===================================================================
            # psutil.cpu_stats() returns CPU statistics as a tuple.
            #===================================================================
            print("******printing the mounted disk partitions******");
            print(psutil.disk_partitions(),"\n");
            #===================================================================
            # psutil.disk_partitions() returns all the mounted disk partitions as a tuple.
            #===================================================================
            print("--------------printing the CPU frequency----------");
            print(psutil.cpu_freq(),"\n");
            #===================================================================
            # psutil.cpu_freq() returns frequency as a named tuple. Here , the current frequency , minimum and the maximum frequencies are expressed in Mhz.
            #===================================================================

            print("######printing the system memory usage#######");
            print(psutil.virtual_memory(),"\n");
            #===================================================================
            # psutil.virtual_memory() returns statistics about the system memory in bytes.
            #===================================================================
            print ("printing the system input output statistics");
            print(psutil.disk_io_counters(),"\n");
            #===================================================================
            # psutil.disk_io_counters() returns system-wide input output statistics as a named tuple.
            #===================================================================
            print("printing the system boot time");
            print(psutil.boot_time(),"\n");
            #===================================================================
            # psutil.boot_time() returns the system boot time in seconds.
            #===================================================================
            print("printing the users connected to the system");
            print(psutil.users(),"\n");
            #===================================================================
            # psutil.users() returns the users currently connected to the system as a list of tuples.
            #===================================================================
            print("----------------------------");
            
            
            
            sleep(5);
            #===================================================================
            # The sleep() suspends the execution for the fixed number of seconds.
            #===================================================================
            
            
            
    def enableThread(self):
        self.en_thread=True;
#===============================================================================
# Here, the en_thread flag is set to True.The en_thread flag is set to True inside a method called enableThread
#===============================================================================
    

     
     
    
     
         
         
         
         
     
         
         
         
    
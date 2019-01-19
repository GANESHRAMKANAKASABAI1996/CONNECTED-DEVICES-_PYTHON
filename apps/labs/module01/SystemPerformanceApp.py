'''
Created on Jan 18, 2019

@author: GANESHRAM KANAKASABAI
'''

from time import sleep
from labs.module01 import SystemPerformanceAdaptor

system_performance=SystemPerformanceAdaptor.SystemPerformanceAdaptor("performance calculation",10);
system_performance.daemon = True
#===============================================================================
# system_performance.daemon = True creates the daemon thread.When the program quits,any daemon threads are killed automatically.
#===============================================================================
system_performance.enableThread();

system_performance.start()
#===============================================================================
# system_performance.start() starts the activity of the thread.
#===============================================================================


while True:
    sleep(2);
    #===========================================================================
    # The sleep() suspends the execution for the fixed number of seconds.
    #===========================================================================
    pass
    
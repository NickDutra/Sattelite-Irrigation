# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 14:35:25 2017

@author: solidworks1
"""
from CropConnectTest import Req_Weather_Data
import time
#import IO





def getdata ():
    data_request = Req_Weather_Data('grossielectric','Summer17','28993')
    return data_request.value 
    
def calcruntime (x):
    y = ((x * .54)/1.04)/.044
    return y
   
def local ():
    x = time.localtime()
    return x[4]



while True:
    ETo = getdata()
    runtime = calcruntime(.118)
    current = time.localtime()
    print "Ready"
    startvar = raw_input()
    if startvar == 'start':
        start =1
        while local() != int(current[4] + runtime):
            print 'Q on'
            print 'Current Min:' + str(current[4])
            print 'Target Min:' + str(int(current[4] + runtime))
            time.sleep(2)
            if local() == int(current[4] + runtime):
                print 'Q off'
                print 'tsime elapsed'
                startvar = ''
                start = 0
                exit 
    
            
        

    
    
        

        

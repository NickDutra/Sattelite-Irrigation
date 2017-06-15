# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 14:35:25 2017

@author: solidworks1
"""
from CropConnectTest import Req_Weather_Data
import time
import IO
#import schedule


autostart=0

def getdata ():
    data_request = Req_Weather_Data('grossielectric','Summer17','28993')
    return data_request.value 
    
def calcruntime (x):
    y = ((x * .54)/1.04)/.044
    return y
    
#schedule.every(1).minute.do()


while True:
    #schedule.run_pending()
    time.sleep(1)
    ETo = getdata()
    runtime = calcruntime(.118)
    print runtime
    if IO.I1():
        print 'Input High'
        IO.Q1(1)
    else:
        print 'Input Low'
        IO.Q1(0)
    
    
    
    
        

        

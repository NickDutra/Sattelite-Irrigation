# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:12:52 2017

@author: solidworks1
"""

from CropConnectTest import Req_Weather_Data
from datetime import datetime, timedelta
import IO





def getdata ():
    data_request = Req_Weather_Data('grossielectric','Summer17','28993')
    return data_request.value 
    
def calcruntime (x):
    y = ((x * .54)/1.04)/.044
    return y
   
def local ():
    x = format(datetime.now(), '%H:%M:%S')
    return x



while True:
    ETo = getdata()
    duration = calcruntime(ETo)
    endtime = datetime.now() +timedelta(seconds=duration)
    endtime = format(endtime, '%H:%M:%S')
    if IO.Q1 and IO.Q2:
        print 'Start'
        while format(datetime.now(),'%H:%M:%S') != endtime:
            IO.Q1(1)
            if format(datetime.now(),'%H:%M:%S') == endtime:
                IO.Q1(0)
                print 'Done'
                exit 
    
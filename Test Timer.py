# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 11:23:07 2017

@author: solidworks1
"""

import time

#Crop Connect Login & Extracting of Session ID
print time.localtime(None)


while True:
    current_time = time.localtime(None)
    Current_hour = current_time[3]
    Current_minute = current_time[4]
    Current_second = current_time[5]
    
    print Current_second
    time.sleep(1)
    
    if Current_second == 40:
        print 'Timer Engaged!'
        print Current_hour, Current_minute, Current_second


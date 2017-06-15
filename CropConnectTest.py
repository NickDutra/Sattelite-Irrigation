# -*- coding: utf-8 -*-
"""
Irrigation Controller 
CropConnect Interface

"""
import requests
import re

#Crop Connect Login & Extracting of Session ID

class Req_Weather_Data:
    
    value = float
    
    def __init__(self, usern, password, node_id):
        self.usern = usern
        self.password = password
        self.node_id = node_id	
        login = requests.get('http://northvalley.cropconnect.com/addUPI?function=login&user='+usern+'&passwd='+password)
        loginstring = str(login.text)    
        idsearch = re.search('ing>(.+?)</', loginstring)
        if idsearch:
            sessionid = idsearch.group(1)
#UPI Request and Daily ETo storing into a local variable
            getdata = 'http://northvalley.cropconnect.com/addUPI?function=getdata&session-id=<SESSION-ID>&id=28993'
            datarequest = re.sub('<SESSION-ID>', sessionid, getdata)
            getdata = requests.get(datarequest)
            ccresponse = str(getdata.text)
            datasearch = re.search('s=...>(.+?)</v', ccresponse)
            if datasearch:
                sETo = datasearch.group(1)
                Req_Weather_Data.value = float(sETo)
#logout of Crop Connect Database
                requests.get('http://northvalley.cropconnect.com/addUPI?function=logout&session-id='+sessionid+'&id=28993')
                        

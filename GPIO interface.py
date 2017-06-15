# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 08:45:44 2017

@author: solidworks1
"""

import RPi.GPIO as GPIO
import Adafruit_GPIO.MCP230xx as MCP230
mcp = MCP230.MCP23008()

#mcp.output(8,1)


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_UP)
I1 = 4
I2 = 17
I3 = 27







while (True):
    if not GPIO.input(I1):
        print 'Input High'
    if not GPIO.input(I2):
        print 'Input 17 High'
    if not GPIO.input(I3):
        print 'Input 24 High'

GPIO.cleanup()
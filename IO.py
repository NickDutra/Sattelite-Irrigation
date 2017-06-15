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


def I1():
    if not GPIO.input(4):
        return 1
    else: 
        return 0
    
def I2():
    if not GPIO.input(17):
        return 1
    else: 
        return 0
    
def I3():
    if not GPIO.input(22):
        return 1
    else: 
        return 0
    
def I4():
    if not GPIO.input(27):
        return 1
    else: 
        return 0
    
def I5():
    if not GPIO.input(23):
        return 1
    else: 
        return 0
    
def Q1(x):
    if x:
        mcp.output(8,1)
    else:
        mcp.output(8,0)
    


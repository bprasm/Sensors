#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
RoAPin = 17 # pin11
RoBPin = 19 # pin12
globalCounter = 0
flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0
def setup():
    GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
    GPIO.setup(RoAPin, GPIO.IN) # input mode
    GPIO.setup(RoBPin, GPIO.IN)
def rotaryDeal():
    global flag
    global Last_RoB_Status
    global Current_RoB_Status
    global globalCounter
    Last_RoB_Status = GPIO.input(RoBPin)
while(not GPIO.input(RoAPin)):
    Current_RoB_Status = GPIO.input(RoBPin)
    flag = 1
    if flag == 1:
        flag = 0
    if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
        globalCounter = globalCounter + 1
    if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
        globalCounter = globalCounter - 1
def loop():
    global globalCounter
    while True:
        rotaryDeal()
        print 'globalCounter = %d' % globalCounter
def destroy():
    GPIO.cleanup() # Release resource
    if __name__ == '__main__': # Program start from here
        setup()
    try:
        loop()
    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
        destroy()

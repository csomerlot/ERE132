#!/usr/bin/env python
from logger import *
from time import sleep

##from mcp3008 import *
from virtual import *

# change these as desired
SPICLK = None
SPIMISO = None
SPIMOSI = None
SPICS = None
Secs = 0

# set up the Serial Peripheral Interface (SPI) pins
GPIO.setup (None, GPIO.OUT)
GPIO.setup (None, GPIO.IN)
GPIO.setup (None, GPIO.OUT)
GPIO.setup (None, GPIO.OUT)


while True: ## infinite loop
    
    lightReading = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
    tempReading  = readadc(1, SPICLK, SPIMOSI, SPIMISO, SPICS)

    #### Do math to convert reading from digital readings to real value
    temp  = tempReading
    light = lightReading

    #### write it out to the data file
    log(temp, light)
    
    sleep(1)


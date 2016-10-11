#!/usr/bin/env python
from logger import *
from time import sleep

##from mcp3008 import *  ### swap these libraries once RPi is wired with sensors
from virtual import *

# change these as needed (change the Nones)
SPICLK = None
SPIMISO = None
SPIMOSI = None
SPICS = None

# set up the Serial Peripheral Interface (SPI) pins (change the Nones)
GPIO.setup (None, GPIO.OUT)
GPIO.setup (None, GPIO.IN)
GPIO.setup (None, GPIO.OUT)
GPIO.setup (None, GPIO.OUT)

log()
log("temp", "light")

while True: ## infinite loop
    
    lightReading = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
    tempReading  = readadc(1, SPICLK, SPIMOSI, SPIMISO, SPICS)

    #### Do the math to convert reading from digital readings to real value
    temp  = tempReading
    light = lightReading

    #### write it out to the data file
    log(temp, light)
    
    sleep(1) # pauses for 1 second


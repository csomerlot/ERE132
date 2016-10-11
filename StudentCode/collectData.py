#!/usr/bin/env python

## Import libraries to help minmize the code you need
from logger import *
from time import sleep

##from mcp3008 import *  ### swap these libraries once RPi is wired with sensors
from virtual import *    ### this is the library used for testing you code, on an RPi or elsewhere

## These constants define the communication pins of the GPIO on the RPi
# change these as needed (change the Nones)
SPICLK = None
SPIMISO = None
SPIMOSI = None
SPICS = None

## These setup function calls tell the RPi which pins are for input, which are for output
# set up the Serial Peripheral Interface (SPI) pins (change the Nones)
GPIO.setup (None, GPIO.OUT)
GPIO.setup (None, GPIO.IN)
GPIO.setup (None, GPIO.OUT)
GPIO.setup (None, GPIO.OUT)

## these log calls set up your log file so taht you can tell what data gets collected
log()
log("temp", "light")

while True: ## infinite loop

    ##  These read calls get a digital value from the ADC chip connected to the RPi's GPIO pins 
    lightReading = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
    tempReading  = readadc(1, SPICLK, SPIMOSI, SPIMISO, SPICS)

    #### Do the math to convert reading from digital readings to real value
    temp  = tempReading
    light = lightReading

    #### write it out to the data file
    log(temp, light)
    
    sleep(1) # pauses for 1 second


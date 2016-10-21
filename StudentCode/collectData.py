#!/usr/bin/env python

## Import libraries to help minmize the code you need
from logger import *
from time import sleep
## import sys
## import Adafruit_GPIO.SPI as SPI
## import Adafruit_GPIO as GPIO
import Adafruit_MCP3008

## from Adafruit_MCP3008 import * ### swap these libraries once RPi is wired with sensors
## from virtual import *        ### this is the library used for testing your code, on an RPi or elsewhere

## These constants define the communication pins of the GPIO on the RPi
SPICLK  = 17
SPIMISO = 18
SPIMOSI = 23
SPICS   = 24
mcp = Adafruit_MCP3008.MCP3008(SPICLK, SPICS, SPIMISO, SPIMOSI)

## These setup function calls tell the RPi which pins are for input, which are for output
##GPIO.setup(SPIMOSI, GPIO.OUT)
##GPIO.setup(SPIMISO, GPIO.IN)
##GPIO.setup(SPICLK, GPIO.OUT)
##GPIO.setup(SPICS, GPIO.OUT)

## these log calls set up your log file so that you can tell what data gets collected
log()
log("temp", "light")

while True: ## infinite loop

    ##  These read calls get a digital value from the ADC chip connected to the RPi's GPIO pins 
    ## lightReading = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
    ## tempReading  = readadc(1, SPICLK, SPIMOSI, SPIMISO, SPICS)
    lightReading = mcp.read_adc(0)
    tempReading  = mcp.read_adc(1)
    
    #### Do the math to convert reading from digital readings to real value
    tempCelcius  = 100*(3.3 * tempReading / 1024.0) - 50
    light = 100.0 * lightReading / 1024.0 ## % of full light
    roundCelcius = round (tempCelcius, 2)
    roundLight = round (light, 2)
    #### write it out to the data file
    log(roundCelcius, roundLight)
    
    
    sleep(1) # pauses for 1 second


import sys
import os
import datetime
import spidev
import time

#Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

#Function to convert data into a standard range
def ConvertMoisture(data):
    moist_reading = (data * 100) / float(1023)
    moist_reading = round(moist_reading,1)
    #print moist_reading
    return moist_reading




while True:
    
#Get the sensor data
    
    moisture = ReadChannel(1) #Reads CH0 from the MCP3008 chip
    moisture_level = ConvertMoisture(moisture) #Normalises the reading from 0-1023 to 0-100
    print  moisture_level
    time.sleep(5)
    
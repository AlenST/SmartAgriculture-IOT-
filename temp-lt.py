import spidev
import time
import os
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
#Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
#GPIO.setup(1, GPIO.IN)


GPIO.setwarnings (False)
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
#GPIO.setup(0,GPIO.OUT)
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,places)
    return volts
# Define sensor channels
light_channel = 0
# Define delay between readings
delay = 5

#i=GPIO.input(19)

while True:
    # Read the light sensor data
    light_level = ReadChannel(light_channel)
    light_volts = ConvertVolts(light_level,2)
    print("--------------------------------------------")
    print("Light: {} ({}V)".format(light_level,light_volts))
    humidity,temperature = Adafruit_DHT.read_retry(11,17) 
    print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature) 
    if(light_level>=1023 and temperature > 26):
        GPIO.output(13,GPIO.HIGH)       
    else:
        GPIO.output(13,GPIO.LOW)
        
    #asdfg
    # Wait before repeating loop
    time.sleep(delay)

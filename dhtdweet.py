#!/usr/bin/python
import sys
import Adafruit_DHT
import time
import requests
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
dweetIO = "https://dweet.io/dweet/for/"
myName = "Testing yoyo"
myKey3 = "Average_Temperature"
myKey4 = "Average_Humidity"
while True:
    sumt=0
    sumh = 0
    humidity, temperature = Adafruit_DHT.read_retry(11, 2)

    print 'Temp: {0:0.2f} *C  Humidity: {1:0.2f} %HM'.format(temperature, humidity)
    time.sleep(0.1)

    humidity1, temperature1 = Adafruit_DHT.read_retry(11, 3)

    print 'Temp1: {0:0.2f} *C  Humidity1: {1:0.2f} %HM'.format(temperature1, humidity1)
    time.sleep(0.1)

    sumt=temperature+temperature1
    sumh=humidity+humidity1
    Average_Temperature =sumt/2
    Average_Humidity=sumh/2
    rqsString = dweetIO+myName+'?'+myKey3+'='+str(Average_Temperature)
    print(rqsString)
    rqs = requests.get(rqsString)
    rqsString = dweetIO+myName+'?'+myKey4+'='+str(Average_Humidity)
    print(rqsString)
    rqs = requests.get(rqsString)
    print 'Avg Temp: {0:0.2f} *C Avg Hum: {1:0.2f} %HM\n'.format(Average_Temperature,Average_Humidity) 

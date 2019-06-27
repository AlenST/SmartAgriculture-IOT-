#RELAY RUNNING ON DHT-11 CONDITIONS >28C

import time
import sys
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setwarnings(False)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 20)

    print 'Temp: {0:0.2f} *C  Humidity: {1:0.2f} %HM'.format(temperature, humidity)
    time.sleep(0.1)
    
    if temperature>30:
        print "falling edge detected on 25"
        GPIO.output(21,GPIO.HIGH)
        
    else:
        GPIO.output(21,GPIO.LOW)
        
    
    

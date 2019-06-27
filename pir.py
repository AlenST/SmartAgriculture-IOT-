import RPi.GPIO as GPIO
import requests
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
dweetIO = "https://dweet.io/dweet/for/"
myNamep = "dsusmartagriculture101pir"
myKey1 = "pir1"
myKey2 = "pir2"
myKey3 = "pir3"
myKey4 = "pir4"
GPIO.setup(35, GPIO.IN)
GPIO.setup(36, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(38, GPIO.IN)
#Read output from PIR motion sensor
#GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
       i=GPIO.input(35)
       if i==0:                 #When output from motion sensor is LOW
             print "No  intruders1",i
             rqsString = dweetIO+myNamep+'?'+myKey1+'='+str(i)
             print(rqsString)
             rqs = requests.get(rqsString)
             #GPIO.output(3, 0)  #Turn OFF LED
             #time.sleep(1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             rqsString = dweetIO+myNamep+'?'+myKey1+'='+str(i)
             print(rqsString)
             rqs = requests.get(rqsString)
             #GPIO.output(3, 1)  #Turn ON LED
             #time.sleep(1)
       i=GPIO.input(36)
       if i==0:                 #When output from motion sensor is LOW
             print "No  intruders1",i
             rqsString = dweetIO+myNamep+'?'+myKey2+'='+str(i)
             print(rqsString)
             rqs = requests.get(rqsString)
             #GPIO.output(3, 0)  #Turn OFF LED
             #time.sleep(1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             rqsString = dweetIO+myNamep+'?'+myKey2+'='+str(i)
             print(rqsString)
             rqs = requests.get(rqsString)
             #GPIO.output(3, 1)  #Turn ON LED
             #time.sleep(1)
       i=GPIO.input(37)
       if i==0:                 #When output from motion sensor is LOW
             print "No  intruders1",i
             rqsString = dweetIO+myNamep+'?'+myKey3+'='+str(i)
             print(rqsString)
             rqs = requests.get(rqsString)
             #GPIO.output(3, 0)  #Turn OFF LED
             #time.sleep(1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             rqsString = dweetIO+myNamep+'?'+myKey3+'='+str(i)
             print(rqsString)
             rqs = requests.get(rqsString)
             #GPIO.output(3, 1)  #Turn ON LED
             #time.sleep(1)
       i=GPIO.input(38)
       if i==0:                 #When output from motion sensor is LOW
             print "No  intruders1",i
             rqsString = dweetIO+myNamep+'?'+myKey4+'='+str(i)
             print(rqsString)
             rqs = requests.get(rqsString)
             #GPIO.output(3, 0)  #Turn OFF LED
             #time.sleep(1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             rqsString = dweetIO+myNamep+'?'+myKey4+'='+str(i)
             print(rqsString)
             rqs = requests.get(rqsString)
             #GPIO.output(3, 1)  #Turn ON LED
             #time.sleep(1)
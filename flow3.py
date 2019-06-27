import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
currentTime =  int(round(time.time() * 1000))
cloopTime = currentTime


global count
count = 0

def countPulse(channel):
    global count
   
    count = count+1
    print count
   #if(currentTime >= (cloopTime + 1000)):
   
    cloopTime = currentTime #Updates cloopTime
    # Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
    l_hour = (count * 60 / 7.5)# (Pulse frequency x 60 min) / 7.5Q = flowrate in L/hour
    count = 0 # Reset Counter
    print l_hour# Print litres/hour
    print" L/hour"
   

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()

import os
import time
import datetime
import glob
import MySQLdb
from time import strftime
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Variables for MySQL
db = MySQLdb.connect(host="localhost", user="root",passwd="root", db="smartagri")
cur = db.cursor()
 
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.2f} *C  Humidity: {1:0.2f} %HM'.format(temperature, humidity)
    time.sleep(3)
 
while True:
    
    print temperature
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    print datetimeWrite
    sql = ("""INSERT INTO sensorlog (datetime,temperature) VALUES (%s,%s)""",(datetimeWrite,temperature))
    try:
        print "Writing to database..."
        # Execute the SQL command
        cur.execute(*sql)
        # Commit your changes in the database
        db.commit()
        print "Write Complete"
 
    except:
        # Rollback in case there is any error
        db.rollback()
        print "Failed writing to database"
 
    cur.close()
    db.close()
    break


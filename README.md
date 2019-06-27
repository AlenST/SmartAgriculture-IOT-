# **Smart Agriculture : An IoT approach**

## **Problem Statement** :
**INDIA** is an agrarian economy, a country where more than seventy percent of the citizens are dependent on agriculture.
 Food production must increase by 70% by 2050, and this has to be achieved with available limited resources.
One way to address this issue is by making farms more connected and intelligent.-**PRECISION FARMING OR SMART FARMING**.

------------------------
## **Abstract** :

IoT based Smart Farming system for Smarter and judicious Irrigation of the fields, intruder alert systems and real time in-farm weather monitoring which helps reduce wastage, effective use of water and thus increase the yield of the crops. The integration of traditional methodology with latest technologies such as Internet of Things helps us solve this problem. In this work, a system is used to monitor the fields using sensors( soil moisture, humidity, temperature) and thus automate the irrigation system in the fields. 
As statistics say, this system will be more efficient than
conventional irrigation methodologies.

_____

## **Proposed Solution** :
The project consists of the following sub modules:
* SMART IRRIGATION  SYSTEM 
* WATER LEVEL MONITORING 
* FIELD MONITORING SYSTEM
* WEATHER MONITORING SYSTEM
* REALTIME DASHBOARD FOR MONITORING THE FARMS 
* REALTIME APACHE SERVER TO STORE SENSOR DATA
____

## **Working** :
A single board computer known as Raspberry Pi is what we use as the interface between the sensors and the internet. The data collected from the respective sensors are sent to a web based MySQL administrator called phpMyAdmin and from there, the data goes to a real time dashboard which is easily accessible from any part of the world. The dashboard used is an open source platform called Freeboard.io. The farmers' can able to monitor the field conditions from anywhere. And simultaneously keep receiving timely SMSs about the sensor activity in the fields with the help of a GSM Module.
____

## **Block Diagram** :
![Block Diagram](/images/BlockDiagram.JPG)
_______
## **Screenshots** :

**DASHBOARD**
![Dashboard](/images/dashboard.png)

**DATABASE**
![Database](/images/database1.png)
![Database](/images/database2.png)

**WEATHER UPDATE**
![Weather](/images/weather.png)

_______

## **References** :
1. [DHT Sensor](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)
2. [GSM Sensor](https://www.cooking-hacks.com/index.php/documentation/tutorials/gprs-gsm-quadband-module-arduino-raspberry-pi-tutorial-sim-900/)
3. [Soil Moisture Sensor](https://www.modmypi.com/blog/raspberry-pi-plant-pot-moisture-sensor-with-email-notification-tutorial)
4. [PIR Sensors](https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio)
5. [Ultrasonic Sensor](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi) 
6. [Apache Server](https://pimylifeup.com/raspberry-pi-mysql-phpmyadmin/)
7. [Dashboard](https://freeboard.io/)

________

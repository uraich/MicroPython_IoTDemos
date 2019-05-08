from umqtt.simple import MQTTClient
from machine import Pin
import network
import time,sys

#wifi setting
SSID="WIFI_SSID" #insert your wifi ssid
PASSWORD="WIFI_PASSWORD" #insert your wifi password

SERVER = "mqtt.mydevices.com"
CLIENT_ID = "CAYENNE_CLIENT_ID" #insert your client ID
username='CAYENNE_USERNAME' #insert your MQTT username
password='CAYENNE_PASSWORD' #insert your MQTT password

TOPIC = ("v1/%s/things/%s/data/1" % (username, CLIENT_ID))

if sys.platform == "esp8266":
    print("cayenneButton running on ESP8266")
    button = Pin(0,Pin.IN,Pin.PULL_UP)
else:
    print("cayenneButton running on ESP32") 
    button = Pin(17,Pin.IN,Pin.PULL_UP)

def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  print('connecting to network...')
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  print('network config:', wlan.ifconfig())

def senddata():
  pbValue=button.value()

  if pbValue == 0:
    c.publish(TOPIC,'digital_sensor,d=1')
    print("The switch is pressed")
  else:
    c.publish(TOPIC,'digital_sensor,d=0')
    print("The switch is not pressed")
  time.sleep(10)
  
connectWifi(SSID,PASSWORD)
server=SERVER
print("Connecting to myDevices MQTT broker")
c = MQTTClient(CLIENT_ID, server,0,username,password)
c.connect()
print("Successfully connected to myDevices MQTT broker")

while True:
    try:
        senddata()
    except OSError:
        pass



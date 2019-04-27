from machine import Pin
from cayenne import Cayenne
import network
import time
import dht

# the device is on GPIO 0

addrOled    = 60  #0x3c
hSize       = 48  # Hauteur ecran en pixels | display heigh in pixels
wSize       = 64  # Largeur ecran en pixels | display width in pixels
oledIsConnected = False
tempChannel=7
humidityChannel=8

# create the dht11 object
dht11=dht.DHT11(Pin(2))

cayenne=Cayenne()
cayenne.mqttConnect()

print("Successfully connected to myDevices MQTT broker")
def senddata():
  print("Measuring...")
  dht11.measure()
  temp = dht11.temperature()
  tempString='temp,c=%6.3f'%temp
  print("Publishing: temperature: %s"%tempString)
  cayenne.publish(str(tempChannel),tempString)
  time.sleep(5)
  humidity=dht11.humidity()
  humidityString='rel_hum,p=%6.3f'%humidity
  print("Publishing humidity: %s"%humidityString)
  cayenne.publish(str(humidityChannel),humidityString)
  time.sleep(5)
  
while True:
#    try:
  senddata()
#    except OSError:
#        pass



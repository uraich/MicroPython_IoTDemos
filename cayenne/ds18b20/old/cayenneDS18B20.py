from machine import Pin
from cayenne import Cayenne
import network
import time
import onewire
import ds18x20

# the device is on GPIO 4
dat =Pin(4)
pinScl      =  5  #ESP8266 GPIO5 (D1)
pinSda      =  4  #ESP8266 GPIO4 (D2)
addrOled    = 60  #0x3c
hSize       = 48  # Hauteur ecran en pixels | display heigh in pixels
wSize       = 64  # Largeur ecran en pixels | display width in pixels
oledIsConnected = False
cayenneChannel=1

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))
# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

cayenne=Cayenne()
cayenne.mqttConnect()

print("Successfully connected to myDevices MQTT broker")
def senddata():
  ds.convert_temp()
  time.sleep_ms(100)
  temp = ds.read_temp(roms[0])
  dataString='temp,c=%6.3f'%temp
  print("Publishing: %s"%dataString)
  cayenne.publish(str(cayenneChannel),dataString)
  time.sleep(10)
  
while True:
    try:
        senddata()
    except OSError:
        pass



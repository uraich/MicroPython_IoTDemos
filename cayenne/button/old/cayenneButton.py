from umqtt.simple import MQTTClient
from machine import Pin
import network
import time

#wifi setting
SSID="SFR_A0F0_EXT" #insert your wifi ssid
PASSWORD="osto7rawayristaxtris" #insert your wifi password

SERVER = "mqtt.mydevices.com"
CLIENT_ID = "dae86710-4ae9-11e9-a6b5-e30ec853fbf2" #insert your client ID
username='7c70a330-69af-11e8-a76a-fdebb8d0010d' #insert your MQTT username
password='32d184add41570759dd1735fa464cef7e62876a4' #insert your MQTT password
#CLIENT_ID="093ef190-2567-11e9-8cb9-732fc93af22b"
#username="7c70a330-69af-11e8-a76a-fdebb8d0010d"
#password="32d184add41570759dd1735fa464cef7e62876a4"
TOPIC = ("v1/%s/things/%s/data/1" % (username, CLIENT_ID))

button=Pin(0,Pin.IN,pull=Pin.PULL_UP) # Declaring button on GPIO 0

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



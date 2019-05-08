efrom umqtt.robust import MQTTClient
from machine import Pin
import network
import time, sys, neopixel

#wifi setting
SSID="WIFI_SSID" #insert your wifi ssid
PASSWORD="WIFI_PASSWORD" #insert your wifi password

SERVER = "mqtt.mydevices.com"
CLIENT_ID = "CAYENNE_CLIENT_ID" #insert your client ID
username='CAYENNE_USERNAME' #insert your MQTT username
password='CAYENNE_PASSWORD' #insert your MQTT password
TOPIC_BASE = ("v1/%s/things/%s/" % (username, CLIENT_ID))

n=1        # number of LEDs
if sys.platform == "esp8266":
    print("cayenneWS2812B running on ESP8266")
    pin = 4   # connected to GPIO 4 on esp8266
else:
    print("cayenneWS2812B running on ESP32") 
    pin = 21   # connected to GPIO 21 on esp32
    
channelRED   = 3
channelGREEN = 2
channelBLUE  = 4

global red,green,blue
red=0
green=0
blue=0
neoPixel = neopixel.NeoPixel(Pin(pin), n)

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
  
# a typical message from Cayenne looks as follows:
# topic:  b'v1/7cxxxxxxxxxxx-yyyy-zzzz-dddddddddd0d/things/33333333-4ddd-1111-yyyy-dddddddddddd/cmd/2'
# the value after /cmd/ is the channel number
# msg:    b'uvtDurLwnJnpGqE,112'
# the value after the ',' is the new slider value

def ledUpdate(topic,msg):
  global red,green,blue
  
  print("Channel red: %d, channel green: %d, channel blue: %d"%(channelRED,channelGREEN,channelBLUE))
  print((topic,msg))
  channelIndex = topic.index(b'cmd')+4              # search for 'cmd' the channel no follows
  print("channelIndex: %d"%channelIndex)
  channel = int(topic[channelIndex:])               # from the channel index to the end
  print("channel: %d"%channel)
  valueIndex = msg.index(b',')+1;
  print("valueIndex: %d"%valueIndex)
  value = int(msg[valueIndex:])
  print("value: %d"%value)
  print("red: %d"%red)
  # now set the new value on the rgb LED

  if channel == channelRED:
    print("red")
    print("value: %d"%value)
    red=value

  if channel == channelGREEN:
    green=value
  if channel == channelBLUE:
    blue = value
  print("red: %d, green: %d, blue: %d"%(green,red, blue))

  print("before writing LED")
  neoPixel[0] = (green, red, blue)
  neoPixel.write() 
  
def subscribeCayenne(channel):
  topic= TOPIC_BASE + 'cmd/%d'%channel
  print("Subscribing to topic %s, please wait 5 s"%topic)
  time.sleep(0.5)
  c.subscribe(topic)
  print("Subscribe sent")
  
# switch the LED off, it is too bright!

neoPixel[0] = (red, green, blue)
neoPixel.write()

connectWifi(SSID,PASSWORD)
server=SERVER
print("Connecting to myDevices MQTT broker")
c = MQTTClient(CLIENT_ID, server,0,username,password)
print("Registering callback")
c.set_callback(ledUpdate)
if not c.connect(clean_session=False):
  print("New session being set up")
  subscribeCayenne(2)
  subscribeCayenne(3)
  subscribeCayenne(4)
  
while True:
    try:
        print("Wait for mgs")
        c.wait_msg()
    except OSError:
        pass





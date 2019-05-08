#
# cayenneWS2812B.py
# The WS2812B is an rgb LED whose color components can be controlled through
# sliders in Cayenne. The program registers a command callback and, dependant
# on the channel employed, sets the corresponding color component
# 
# copyright U. Raich
# This is a demo program for the workshop on IoT at the African Internet Summit 2019
# Released under GPL
#
from machine import Pin
import neopixel
import cayenne.client
import time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USERNAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

TOPIC_BASE = ("v1/%s/things/%s/" % (MQTT_USERNAME, MQTT_CLIENT_ID))
global redChannel,blueChannel,greenChannel

n=1          # no of LEDS
pin=4        # connected to GPIO 4
channelRED   = 3
channelGREEN = 2
channelBLUE  = 4
global red,green,blue
red=0
green=0
blue=0

neoPixel = neopixel.NeoPixel(Pin(pin), n)

# switch the LED off, it is too bright!

neoPixel[0] = (green, red, blue)
neoPixel.write()

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
  print("red: %d, green: %d, blue: %d"%(red,green,blue))

  print("before writing LED")
  neoPixel[0] = (green, red, blue)
  neoPixel.write()
  
def subscribeCayenne(channel):
  topic= TOPIC_BASE + 'cmd/%d'%channel
  print("Subscribing to topic %s, please wait 5 s"%topic)
  time.sleep(0.5)
  client.client.subscribe(topic)
  print("Subscribe sent")
  
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
# register callback
client.client.set_callback(ledUpdate)
#client.on_message=ledUpdate
if not client.client.connect(clean_session=False):
  print("New session being set up")
  subscribeCayenne(2)
  subscribeCayenne(3)
  subscribeCayenne(4)
  
while True:
    try:
        print("Wait for mgs")
        client.client.wait_msg()
    except OSError:
      print("OS error")


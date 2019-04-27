from umqtt.robust import MQTTClient
from machine import Pin
import network
import time, neopixel

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
TOPIC_BASE = ("v1/%s/things/%s/" % (username, CLIENT_ID))

n=1        # number of LEDs
pin = 4    # connected to GPIO 4
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
# topic:  b'v1/7c70a330-69af-11e8-a76a-fdebb8d0010d/things/dae86710-4ae9-11e9-a6b5-e30ec853fbf2/cmd/2'
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
  print("red: %d, green: %d, blue: %d"%(red,green,blue))

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





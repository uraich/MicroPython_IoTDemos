from machine import Pin,ADC
from cayenne import Cayenne
import network
import time

# the illumination LED is on GPIO 16
# the built-in LED on GPIO 2
# the photo-resistor on ADC A0

addrOled    = 60  #0x3c
hSize       = 48  # Hauteur ecran en pixels | display height in pixels
wSize       = 64  # Largeur ecran en pixels | display width in pixels
oledIsConnected = False
cayenneChannel=1
# Cayenne definitions
username='7c70a330-69af-11e8-a76a-fdebb8d0010d'
CLIENT_ID="d6accfc0-6541-11e9-bdb5-dfd20f02ea3f"
TOPIC_BASE = ("v1/%s/things/" % username)

intensityChannel=1
illuminationLedChannel=2
indicatorLedChannel=3

# create adc and the led object
adc = ADC(0)
illuminationLed = Pin(16,Pin.OUT)
global count,ledValue
count=0
ledValue=0
# switch LED off
illuminationLed.value(ledValue)

cayenne=Cayenne(CLIENT_ID)
cayenne.mqttConnect()

print("Successfully connected to myDevices MQTT broker")

def ledSwitch(topic,msg):
  print(topic,msg)
  
def subscribeCayenne(clientID,channel):
  topic= TOPIC_BASE + clientID +'/cmd/%d'%channel
  print("Subscribing to topic %s, please wait 5 s"%topic)
  time.sleep(0.5)
  client.subscribe(topic)
  print("Subscribe sent")

def senddata():
  global count,ledValue
  lightIntensity = adc.read()
  print("Light intensity value from ADC: %d"%lightIntensity);
  print("Count: %d"%count)
  print("led value: %d"%ledValue)
  intensityString = "voltage,mv=%d"%lightIntensity
  cayenne.publish(str(intensityChannel),intensityString)
  time.sleep(2)
  count+=1
  if count > 2:
    if ledValue == 0:
      ledValue = 1
    else:
      ledValue = 0;
    illuminationLed.value(ledValue)
    count = 0
    
client=cayenne.getClient()
client.set_callback(ledSwitch)
subscribeCayenne(CLIENT_ID,illuminationLedChannel)

while True:
    try:
        if client.check_msg():
          print("Message seen");
        senddata()
    except OSError:
        pass




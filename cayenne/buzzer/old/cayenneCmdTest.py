# cayenneCmdTest: gets a number from a PC program via Cayenne and prints the value
# This program is a test program on the way to a simple RTTTL song player
# The PC program sends a song number and the buzzer will play that song
# copyright Uli Raich 10.4.2019
# This program was developed for the AFNOG-2019 workshop on IoT
# It is released under GPL
# 
from cayenne import Cayenne
import sys,time
SERVER = "mqtt.mydevices.com"
CLIENT_ID = "CAYENNE_CLIENT_ID" #insert your client ID
username='CAYENNE_USERNAME' #insert your MQTT username
password='CAYENNE_PASSWORD' #insert your MQTT password

laptopClient="LAPTOP_CLIENT_ID"

TOPIC_BASE = ("v1/%s/things/" % username)
cayenne=Cayenne()
cayenne.mqttConnect()

def cmdUpdate(topic,msg):
    print("Update")
    print(topic,msg)

def subscribeCayenne(clientID,channel):
  topic= TOPIC_BASE + clientID +'/cmd/%d'%channel
  print("Subscribing to topic %s, please wait 5 s"%topic)
  time.sleep(0.5)
  client.subscribe(topic)
  print("Subscribe sent")
    
client=cayenne.getClient()
client.set_callback(cmdUpdate)
subscribeCayenne(laptopClient,1)

while True:
    try:
        print("Wait for mgs")
        client.wait_msg()
    except OSError:
        pass





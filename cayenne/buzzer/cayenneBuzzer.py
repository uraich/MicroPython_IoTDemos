# cayenneCmdTest: gets a number from a PC program via Cayenne and prints the value
# This program is a test program on the way to a simple RTTTL song player
# The PC program sends a song number and the buzzer will play that song
# copyright Uli Raich 10.4.2019
# This program was developed for the AFNOG-2019 workshop on IoT
# It is released under GPL
#

from machine import Pin,PWM
from rtttl import RTTTL
import songs
import cayenne.client
import sys,time
import logging

MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID" #insert your client ID
MQTT_USERNAME='CAYENNE_USERNAME' #insert your MQTT username
MQTT_PASSWORD='CAYENNE_PASSWORD' #insert your MQTT password

laptopClient="LAPTOP_CLIENT_ID"

if sys.platform == "esp8266":
    print("cayenneBuzzer running on ESP8266")
    pwmPin = 14
else:
    print("cayenneBuzzer running on ESP32") 
    pwmPin = 18
    
speaker_pin=Pin(pwmPin)

speaker = PWM(speaker_pin)
musicChannel = 1

songList={
    1:'Super Mario - Main Theme',
    2:'Super Mario - Title Music',
    3:'SMBtheme',
    4:'SMBwater',
    5:'SMBunderground',
    6:'The Simpsons',
    7:'Indiana',
    8:'TakeOnMe',
    9:'Entertainer',
    10:'Muppets',
    11:'Xfiles',
    12:'Looney',
    13:'20thCenFox',
    14:'Bond',
    15:'MASH',
    16:'StarWars',
    17:'GoodBad',
    18:'TopGun',
    19:'A-Team',
    20:'Flinstones',
    21:'Jeopardy',
    22:'Smurfs',
    23:'MahnaMahna',
    24:'LeisureSuit',
    25:'MissionImp'
}

TOPIC_BASE = ("v1/%s/things/" % MQTT_USERNAME)
client = cayenne.client.CayenneMQTTClient(True)
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)


def play_tone(freq, msec):
#    print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    print("Freq: %6.1f, duration: %6.1f"%(freq,msec))
    if freq > 0:
        speaker.freq(int(freq))     # Set frequency
        speaker.duty(512)           # 50% duty cycle
    time.sleep(msec*0.001)  # Play for a number of msec
    speaker.duty(0)                 # Stop playing
    time.sleep(0.05)            # Delay 50 ms between notes

def getSongNumber(message):
    print(message)
    msg = cayenne.client.CayenneMessage(message[0],message[1])
    if msg.channel == musicChannel:
        # extract the song number
        print(msg.value)        
        songNo = int(msg.value.split("=")[1])
        print("song number: %d"%songNo)
        songName = songList.get(songNo)    
        print('Playing the song: %s'%songName)
        # play the tune
        tune = RTTTL(songs.find(songName))
        for freq, msec in tune.notes():
            play_tone(freq, msec)
            
def subscribeCayenne(clientID,channel):
  topic= TOPIC_BASE + clientID +'/cmd/%d'%channel
  print("Subscribing to topic %s, please wait 5 s"%topic)
  time.sleep(0.5)
  client.client.subscribe(topic)
  print("Subscribe sent")
  
# subscribe cmd messages from the laptop client
subscribeCayenne(laptopClient,1)

client.on_message = getSongNumber
client.loop_forever()
#while True:
    #try:
        #print("Wait for mgs")
        #client.wait_msg()
    #except OSError:
        #pass





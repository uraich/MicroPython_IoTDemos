# cayenneCmdTest: gets a number from a PC program via Cayenne and prints the value
# This program is a test program on the way to a simple RTTTL song player
# The PC program sends a song number and the buzzer will play that song
# copyright Uli Raich 10.4.2019
# This program was developed for the AFNOG-2019 workshop on IoT
# It is released under GPL
#

from cayenne import Cayenne
from machine import Pin,PWM
from rtttl import RTTTL
import songs
import sys,time

SERVER = "mqtt.mydevices.com"
CLIENT_ID = "CAYENNE_CLIENT_ID" #insert your client ID
username='CAYENNE_USERNAME' #insert your MQTT username
password='CAYENNE_PASSWORD' #insert your MQTT password

laptopClient="LAPTOP_CLIENT_ID"

PWM_PIN=14
speaker_pin=Pin(PWM_PIN)
speaker = PWM(speaker_pin)

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

TOPIC_BASE = ("v1/%s/things/" % username)
cayenne=Cayenne()
cayenne.mqttConnect()

def play_tone(freq, msec):
#    print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    print("Freq: %6.1f, duration: %6.1f"%(freq,msec))
    if freq > 0:
        speaker.freq(int(freq))     # Set frequency
        speaker.duty(512)           # 50% duty cycle
    time.sleep(msec*0.001)  # Play for a number of msec
    speaker.duty(0)                 # Stop playing
    time.sleep(0.05)            # Delay 50 ms between notes

def getSongNumber(topic,msg):
    print("Update")
    print(topic,msg)
    channelIndex = topic.index(b'cmd')+4              # search for 'cmd' the channel no follows
    print("channelIndex: %d"%channelIndex)
    channel = int(topic[channelIndex:])               # from the channel index to the end
    print("channel: %d"%channel)
    valueIndex = msg.index(b'=')+1;
    print("valueIndex: %d"%valueIndex)
# extract the song number
    songNo = int(msg[valueIndex:])
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
  client.subscribe(topic)
  print("Subscribe sent")

client=cayenne.getClient()
client.set_callback(getSongNumber)
subscribeCayenne(laptopClient,1)

while True:
    try:
        print("Wait for mgs")
        client.wait_msg()
    except OSError:
        pass





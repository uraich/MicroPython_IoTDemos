from machine import Pin,PWM
import time

from rtttl import RTTTL
import songs

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
def play_tone(freq, msec):
#    print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    print("Freq: %6.1f, duration: %6.1f"%(freq,msec))
    if freq > 0:
        speaker.freq(int(freq))     # Set frequency
        speaker.duty(512)           # 50% duty cycle
    time.sleep(msec*0.001)  # Play for a number of msec
    speaker.duty(0)                 # Stop playing
    time.sleep(0.05)            # Delay 50 ms between notes

songName=songList.get(1)
print('Playing %s'%songName)
tune = RTTTL(songs.find(songName))

for freq, msec in tune.notes():
    play_tone(freq, msec)



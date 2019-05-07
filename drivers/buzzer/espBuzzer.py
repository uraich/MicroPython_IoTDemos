from machine import Pin,PWM
import time

from rtttl import RTTTL
import songs
import sys



print("Testing the buzzer")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

if sys.platform == "esp8266":
    print("Running on ESP8266")
    pwmPin = 14
else:
    print("Running on ESP32") 
    pwmPin = 18
    

speaker_pin=Pin(pwmPin)
speaker = PWM(speaker_pin)
def play_tone(freq, msec):
#    print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    print("Freq: %6.1f, duration: %6.1f"%(freq,msec))
    if freq > 0:
        speaker.freq(int(freq))     # Set frequency
        speaker.duty(512)           # 50% duty cycle
	time.sleep(msec*0.001)  # Play for a number of msec
    speaker.duty(0)                 # Stop playing
    time.sleep(0.05)            # Delay 50 ms between notes

tune = RTTTL(songs.find('Entertainer'))

for freq, msec in tune.notes():
    play_tone(freq, msec)



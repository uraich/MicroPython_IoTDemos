# controls the ws2812b rgb LED
# U. Raich, 19.3.2019
# This program was written as a demo for the AIS conference 2019, Kampala, Uganda

import machine, neopixel, time, sys

n=1        # number of LEDs

print("Testing the push button")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

if sys.platform == "esp8266":
    print("Running on ESP8266")
    pin = 4   # connected to GPIO 4 on esp8266
else:
    print("Running on ESP32") 
    pin = 21   # connected to GPIO 21 on esp32
    
neoPixel = neopixel.NeoPixel(machine.Pin(pin), n)
for i in range (0,250,50):
    for j in range(0,250,50):
        for k in range(0,250,50):
            neoPixel[0] = (i, j, k)
            neoPixel.write()
            time.sleep(0.2)
            print("r,g,b: %d %d %d"%(i,j,k))

neoPixel[0] = (0, 0, 0)
neoPixel.write()





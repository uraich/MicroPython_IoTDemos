# controls the ws2812b rgb LED
# U. Raich, 19.3.2019
# This program was written as a demo for the AIS conference 2019, Kampala, Uganda

import machine, neopixel, time, sys

n=1        # number of LEDs

if sys.platform == "esp8266":
    pin = 4   # connected to GPIO 4 on esp8266
else:
    pin = 21   # connected to GPIO 21 on esp32
neoPixel = neopixel.NeoPixel(machine.Pin(pin), n)

neoPixel[0] = (0, 0, 0)
neoPixel.write()





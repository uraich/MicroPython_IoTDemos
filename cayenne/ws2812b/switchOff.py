# controls the ws2812b rgb LED
# U. Raich, 19.3.2019
# This program was written as a demo for the AIS conference 2019, Kampala, Uganda

import machine, neopixel, time

n=1        # number of LEDs
pin = 4    # connected to GPIO 4

neoPixel = neopixel.NeoPixel(machine.Pin(pin), n)

neoPixel[0] = (0, 0, 0)
neoPixel.write()





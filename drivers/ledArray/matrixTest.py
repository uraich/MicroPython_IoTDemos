#
# matrix.py a test program for the LED matrix
# a value of 0..63 will light 0 .. 63 LEDs
# written for the workshop on IoT at the
# African Internet Summit 2019, Kampala, Uganda
# Copyright U. Raich
# This program is released under GPL
import time

from ledMatrix import matrix
m = matrix.LedMatrix()
m.clear()
time.sleep(0.5)
m.setLevel(0)
#for i in range(0,64):
#    matrix.setLevel(i)
#    time.sleep(0.1)

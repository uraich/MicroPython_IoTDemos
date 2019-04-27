#!/usr/bin/env python3
# an i2c scanner
# Scans all addresses on the I2C bus and prints the addresses of connected
# modules
# copyright U. Raich 19.3.2019
# This program is released under GPL
# It was written for a workshop on IoT networks at the
# AIS conference 2019, Kampala, Uganda

from machine import *
import time
scl = Pin(5)                 # on the wemos d1 mini scl is connected to GPIO 5
sda = Pin(4)                 # on the wemos d1 mini sda is connected to GPIO 4


i2c = I2C(-1,scl,sda)

chipID=i2c.readfrom_mem(0x77,0xD0,1)
print("chip id: %s"%hex(int.from_bytes(chipID,'big')))

                  


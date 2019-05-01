# sht30 test routine
# U. Raich 25.3.2019

from sht30 import SHT30
import sys

sht30=SHT30()
if not sht30.is_present():
    print("Could not find SHT30 board. Please connect it")
    sys.exit()
else:
    print("Found SHT-30, let's go on")

sht30.reset()
temperature, humidity = sht30.measure()
print('Temperature',temperature,'°C, RH:',humidity,' %')

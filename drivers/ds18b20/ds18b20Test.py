# ds18b20Test.py: reads the temperature from a ds18b20 digital thermometer
# U.Raich 8.5.2019
# This program was written for the workshop of IoT at the
# AIS conference 2019, Kampala, Uganda
# It is released under GPL

from machine import Pin
import time,sys
import onewire, ds18x20

# the device is on GPIO 4 (ESP8266) or GPIO 21 (ESP32)

print("Testing the push button")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

if sys.platform == "esp8266":
    print("Running on ESP8266")
    dat = Pin(4)
else:
    print("Running on ESP32") 
    dat = Pin(21)
    
# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

# loop 10 times and print all temperatures
for i in range(10):
    print('temperatures:', end=' ')
    ds.convert_temp()
    for rom in roms:
        print(ds.read_temp(rom), end=' ')
    print()
    time.sleep_ms(2000)

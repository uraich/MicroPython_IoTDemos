# ds1307Test tests the DS1307 driver
# U. Raich 25.3.2019
#
from machine import *
from ds1307 import *
import sys

pinScl      =  5  #ESP8266 GPIO5 (D1)
pinSda      =  4  #ESP8266 GPIO4 (D2)

addrDS1307=0x68
# dateAndTime: yy mm dd ww hh mm ss 
dateAndTime=(2019,3,25,1,17,51,0)

# init ic2 object
i2c = I2C(scl=Pin(pinScl), sda=Pin(pinSda)) #ESP8266 5/4

# Scan i2c bus and check if DS1307 is connected
print('Scan i2c bus...')
devices = i2c.scan()
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
  ds1307IsConnected=False
  for device in devices: 
    if device == addrDS1307:
      ds1307IsConnected = True
      break
if not ds1307IsConnected:
    print("Could not find the DS1307, please connect the board!")
    sys.exit()
    
ds1307 = DS1307(i2c)
print("Setting time")
print("date and time: %s"%str(dateAndTime))
ds1307.datetime(dateAndTime)
ds1307.halt(False)
readBack=ds1307.datetime()
print(readBack)

# Test the OLED shield featuring the SSD1306 display driver

import machine, time, ssd1306
import sys

print("Testing the ssd1306 OLED display")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")
if sys.platform == "esp8266":
    print("Running on ESP8266")
    pinScl      =  5  #ESP8266 GPIO5 (D1
    pinSda      =  4  #ESP8266 GPIO4 (D2)
else:
    print("Running on ESP32") 
    pinScl      =  22  # SCL on esp32 
    pinSda      =  21  # SDA ON ESP32
    
addrOled    = 60  #0x3c

hSize       = 48  # Hauteur ecran en pixels | display heigh in pixels
wSize       = 64  # Largeur ecran en pixels | display width in pixels

oledIsConnected = False

# init ic2 object
i2c = machine.I2C(scl=machine.Pin(pinScl), sda=machine.Pin(pinSda)) #ESP8266 5/4

# Scan le bus i2c et verifie si le BME280 et l'ecran OLED sont connectes
# Scan i2c bus and check if BME2 and OLDE display are connected
print('Scan i2c bus...')
devices = i2c.scan()
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
  for device in devices: 
    if device == addrOled:
      oledIsConnected = True
      
if oledIsConnected:
  oled = ssd1306.SSD1306_I2C(wSize, hSize, i2c, addrOled)
  oled.fill(0)
  oled.text("192.168.",0,0)
  oled.text("1.150",0,10)
  oled.show()
else:
  print('! No i2c display')
time.sleep_ms(5000)

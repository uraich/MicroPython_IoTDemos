import dht
from machine import Pin,I2C
import ssd1306
import sys,time


print("Testing the dht11 temperature and humidity sensor")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

if sys.platform == "esp8266":
    print("Running on ESP8266")
    d = dht.DHT11(Pin(2))
    pinScl      =  5  #ESP8266 GPIO5 (D1
    pinSda      =  4  #ESP8266 GPIO4 (D2)    
else:
    print("Running on ESP32") 
    d = dht.DHT11(Pin(16))
    pinScl      =  22  # SCL on esp32 
    pinSda      =  21  # SDA ON ESP32
    
addrOled    = 60  #0x3c
hSize       = 48  # Hauteur ecran en pixels | display heigh in pixels
wSize       = 64  # Largeur ecran en pixels | display width in pixels

oledIsConnected = False

# init ic2 object
i2c = I2C(scl=Pin(pinScl), sda=Pin(pinSda)) #ESP8266 5/4

# Scan i2c bus and check if the OLED display is connected

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
    print("OLED display found")
    oled.fill(0)
else:
    print("No OLED display connected")
  
while True:
    d.measure()
    temp=d.temperature()
    hum=d.humidity()
    
    print("Temperature: %d"%temp)
    print("Humidity: %d"%hum)
    oledTemp="T: %d C"%temp
    oledHum="H: %d %%"%hum
    oled.fill(0)
    oled.text("Temperature",0,0)
    oled.text(oledTemp,0,10)
    oled.text("Humidity",0,20)
    oled.text(oledHum,0,30)
    oled.show()
    time.sleep(2)

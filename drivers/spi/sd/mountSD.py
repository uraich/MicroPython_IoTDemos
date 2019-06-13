# Mount the SD card
# Peter hinch 30th Jan 2016
# adapted to the WeMos D1 mini (ESP8266 or ESP32) by Uli Raich
import sys, os, sdcard, machine

if sys.platform == 'esp8266':
    print('SD card on ESP8266')
    SPI_CS = 15
    spi = machine.SPI(1)

elif sys.platform == 'esp32':
    print('SD card on ESP32')
    sck = machine.Pin(18)
    miso= machine.Pin(19)
    mosi= machine.Pin(23)
    SPI_CS = 5
    spi = machine.SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)

spi.init()  # Ensure right baudrate   
sd = sdcard.SDCard(spi, machine.Pin(SPI_CS)) # ESP8266 version
print("Sd card created")

try:
    os.mount(sd, '/sd')
except:
    print("Cannot mount file system on sd card, already mounted?")
#    sys.exit()
print('Filesystem check')
print(os.listdir('/sd'))

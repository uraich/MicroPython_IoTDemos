from umqtt.simple import MQTTClient
from machine import Pin,I2C
import network
import time
import ssd1306

pinScl      =  5  #ESP8266 GPIO5 (D1)
pinSda      =  4  #ESP8266 GPIO4 (D2)
addrOled    = 60  #0x3c
hSize       = 48  # Hauteur ecran en pixels | display heigh in pixels
wSize       = 64  # Largeur ecran en pixels | display width in pixels
oledIsConnected = False

#wifi setting
SSID="your WiFi SSID"           #insert your wifi ssid
PASSWORD="your WiFi password"   #insert your wifi password

SERVER = "mqtt.mydevices.com"
CLIENT_ID = "your Cayenne cliend id"             #insert your client ID
username='your Cayenne user name'                #insert your MQTT username
password='your Cayenne password'                 #insert your MQTT password
TOPIC = ("v1/%s/things/%s/data/" % (username, CLIENT_ID))

class Cayenne:
    def __init__(self):
        # init ic2 object
        i2c = I2C(scl=Pin(pinScl), sda=Pin(pinSda)) #ESP8266 5/4
        # Scan the i2c bus and verify if the OLED sceen is connected
        print('Scan i2c bus...')
        self.devices = i2c.scan()
        if len(self.devices) == 0:
            print("No i2c device !")
        else:
            for self.device in self.devices:
                print("OLED found")
                if self.device == addrOled:
                    self.oled = ssd1306.SSD1306_I2C(wSize, hSize, i2c, addrOled)
                    self.oledIsConnected = True

    def mqttConnect(self):
        global wlan
        wlan=network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.disconnect()
        
        # try to connect to wlan
        print('connecting to network...')
        if self.oledIsConnected:
            self.oled.fill(0)
            self.oled.text("Connect",0,0)
            self.oled.text("to WiFi",0,10)
            self.oled.show()
        wlan.connect(SSID,PASSWORD)
        
        while(wlan.ifconfig()[0]=='0.0.0.0'):
            time.sleep(1)
        print('network config:', wlan.ifconfig())
        
        if self.oledIsConnected:
            self.ipAddress = wlan.ifconfig()[0]
            self.oled.fill(0)
            self.oled.text("IP:",0,0)
            self.oled.text(self.ipAddress[0:8],0,10)
            self.oled.text(self.ipAddress[8:],0,20)
            self.oled.show()

        server=SERVER
        
        self.c = MQTTClient(CLIENT_ID, server,0,username,password)

        self.c.connect()
        if self.oledIsConnected:
            self.oled.text("Cayenne",0,30)
            self.oled.text("MQTT ok",0,40)
            self.oled.show()
            
    def publish(self,channel,data):
        self.c.publish(TOPIC+str(channel),data)

print("name: %s"%__name__)
if __name__ == '__main__':
    print("Running Cayenne Test")
    cayenne=Cayenne()
    cayenne.mqttConnect()

from umqtt.simple import MQTTClient
from machine import Pin,I2C
import network
import time
import ssd1306

pinScl      =  5  #ESP8266 GPIO5 (D1)
pinSda      =  4  #ESP8266 GPIO4 (D2)
addrOled    = 60  #0x3c
hSize       = 48  # Hauteur ecran en pixels | display height in pixels
wSize       = 64  # Largeur ecran en pixels | display width in pixels
oledIsConnected = False

#wifi setting
SSID="SFR_A0F0_EXT" #insert your wifi ssid
PASSWORD="osto7rawayristaxtris" #insert your wifi password

SERVER = "mqtt.mydevices.com"
CLIENT_ID = "dae86710-4ae9-11e9-a6b5-e30ec853fbf2"  #insert your client ID
username='7c70a330-69af-11e8-a76a-fdebb8d0010d'     #insert your MQTT username
password='32d184add41570759dd1735fa464cef7e62876a4' #insert your MQTT password

class Cayenne:
    def __init__(self,client_id=CLIENT_ID):
        self.client_id=client_id
        self.topic= ("v1/%s/things/%s/data/" % (username, self.client_id))
        print('Client ID: %s'%self.client_id)
        print('Topic: %s'%self.topic)
        
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
        
        self.c = MQTTClient(self.client_id, server,0,username,password)

        self.c.connect()
        if self.oledIsConnected:
            self.oled.text("Cayenne",0,30)
            self.oled.text("MQTT ok",0,40)
            self.oled.show()
            
    def publish(self,channel,data):
        self.c.publish(self.topic+str(channel),data)

    def getClient(self):
        return self.c

#if __name__=='builtins'
#    print("Running Cayenne Test")
#    cayenne=Cayenne()
#    cayenne.mqttConnect()
#    client=cayenne.getClient()

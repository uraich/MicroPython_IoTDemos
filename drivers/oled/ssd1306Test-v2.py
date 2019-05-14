# Test the OLED shield featuring the SSD1306 display driver

import machine, time, ssd1306
import sys
from math import sin,cos,pi

print("Testing the ssd1306 OLED display")
print("This version uses pre-calculated sin and cos tables")
print("to speed up the drawing of circles")
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

sinTab = [0.0, 0.12533323356430426, 0.2486898871648548, 0.3681245526846779,
          0.4817536741017153, 0.5877852522924731, 0.6845471059286886,
          0.7705132427757893, 0.8443279255020151, 0.9048270524660196,
          0.9510565162951535, 0.9822872507286886, 0.9980267284282716,
          0.9980267284282716, 0.9822872507286887, 0.9510565162951536,
          0.9048270524660195, 0.844327925502015, 0.7705132427757893,
          0.6845471059286888, 0.5877852522924732, 0.4817536741017152,
          0.36812455268467814, 0.24868988716485524, 0.12533323356430454,
          1.2246467991473532e-16, -0.12533323356430429, -0.24868988716485457,
          -0.3681245526846779, -0.4817536741017154, -0.5877852522924727,
          -0.6845471059286884, -0.7705132427757894, -0.8443279255020153,
          -0.9048270524660198, -0.9510565162951535, -0.9822872507286887,
          -0.9980267284282716, -0.9980267284282716, -0.9822872507286887,
          -0.9510565162951536, -0.9048270524660199, -0.844327925502015,
          -0.7705132427757896, -0.684547105928689, -0.5877852522924734,
          -0.4817536741017161, -0.36812455268467786, -0.24868988716485535,
          -0.12533323356430465]

cosTab = [1.0, 0.9921147013144779, 0.9685831611286311, 0.9297764858882515,
          0.8763066800438636, 0.8090169943749475, 0.7289686274214116,
          0.6374239897486897, 0.5358267949789965, 0.42577929156507266,
          0.30901699437494745, 0.18738131458572474, 0.06279051952931353,
          -0.0627905195293134, -0.1873813145857246, -0.3090169943749471,
          -0.4257792915650727, -0.5358267949789969, -0.6374239897486897,
          -0.7289686274214113, -0.8090169943749473, -0.8763066800438636,
          -0.9297764858882513, -0.968583161128631, -0.9921147013144778, -1.0,
          -0.9921147013144779, -0.9685831611286312, -0.9297764858882515,
          -0.8763066800438635, -0.8090169943749478, -0.7289686274214118,
          -0.6374239897486895, -0.5358267949789963, -0.42577929156507216,
          -0.30901699437494756, -0.18738131458572463, -0.06279051952931321,
          0.06279051952931283, 0.18738131458572427, 0.30901699437494723,
          0.4257792915650718, 0.5358267949789968, 0.6374239897486893,
          0.7289686274214112, 0.8090169943749473, 0.8763066800438631,
          0.9297764858882515, 0.968583161128631, 0.9921147013144778]

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
      
def clear():
    oled.fill(0)

def testDrawLine():
    for i in range(0,wSize,4):
        oled.line(0,0,i,hSize-1,1)
        oled.show()
        time.sleep(0.1)
    for i in range(0,hSize,4):
        oled.line(0,0,wSize-1,hSize-i-4,1)
        oled.show()
        time.sleep(0.1)
        
def drawCircle(orig_x,orig_y,radius):
    for i in range(0,50):
        x = round(radius * cosTab[i]) + orig_x + wSize//2
        y = round(radius * sinTab[i]) + orig_y + hSize //2
        if x < wSize and y < hSize:
            oled.pixel(x,y,1)
        oled.show()
        
def testDrawRect():
    for i in range (0,hSize//2,2):
        oled.rect(i,i,wSize-2*i,hSize-2*i,1)
        oled.show()
        time.sleep(0.1)

def testFillRect():
    for i in range(0,hSize//2,3):
        oled.fill_rect(i,i,i*2,i*2,1)
        oled.show()
        time.sleep(0.1)
 
def drawSin():
    oled.hline(0,hSize//2,wSize,1)
    oled.vline(1,0,hSize,1)
    oled.show()
    for i in range(0,wSize):
        oled.pixel(i,round(-sin(2*pi*i/wSize)*hSize//2)+hSize//2,1)
        oled.show()
    oled.text("sin(x)",wSize//4,hSize//5,1)
    oled.show()
     
if oledIsConnected:
  oled = ssd1306.SSD1306_I2C(wSize, hSize, i2c, addrOled)
  oled.fill(0)
  testDrawLine()
  clear()
  testDrawRect()
  clear()
  testFillRect()
  clear()
  drawCircle(0,0,20)
  drawCircle(15,5,10)
  drawCircle(-10,-15,15)
  drawCircle(5,15,5)
  time.sleep(1)
  clear()
  drawSin()
   
else:
  print('! No i2c display')
time.sleep_ms(5000)

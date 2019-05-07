from machine import ADC,Pin
import time,sys

print("Testing the photo resistor on the prototype board")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

if sys.platform == "esp8266":
    print("Running on ESP8266")
    adc = ADC(0)

else:
    print("Running on ESP32") 
    adc = ADC(Pin(36))
    
while True:
    value = adc.read()
    print("Light intensity value from ADC: %d"%value);
    time.sleep(1)

from machine import Pin,ADC
import time,sys

print("Testing the photo resistor with the led switching ")
print("on and off on the prototype board")
print("Program written for the workshop on IoT at the")
print("African Internet Summit 2019")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

if sys.platform == "esp8266":
    print("Running on ESP8266")
    led = Pin(16,Pin.OUT)
    adc = ADC(0)

else:
    print("Running on ESP32") 
    adc = ADC(Pin(36))
    led = Pin(26,Pin.OUT)

count = 0;
ledValue=0
led.value(ledValue);
while True:
    value = adc.read()
    print("Light intensity value from ADC: %d"%value);
    time.sleep(1)
    count+=1
    if count > 4:
        if ledValue == 0:
            ledValue = 1
        else:
            ledValue = 0;
        led.value(ledValue)
        count = 0


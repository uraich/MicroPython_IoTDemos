from machine import Pin,ADC
import time
led = Pin(16,Pin.OUT)
adc = ADC(0)
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


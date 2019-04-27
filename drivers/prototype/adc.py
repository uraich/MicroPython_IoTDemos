from machine import ADC
import time

adc = ADC(0)
while True:
    value = adc.read()
    print("Light intensity value from ADC: %d"%value);
    time.sleep(1)

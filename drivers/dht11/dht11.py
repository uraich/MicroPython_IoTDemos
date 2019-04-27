import dht
import machine
d = dht.DHT11(machine.Pin(0))

d.measure()
temp=d.temperature()
hum=d.humidity()

print("Temperature: %d"%temp)
print("Humidity: %d"%hum)


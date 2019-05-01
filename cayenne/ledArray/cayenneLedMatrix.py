#
# cayenneLedMatrix.py
# The ledMartrix consists of a 8x8 LED array. The number of LEDs lit is controlled by a
# slider in Cayenne. The program registers a command callback which lights the number of LEDs
# given as value parameter.
# 
# copyright U. Raich
# This is a demo program for the workshop on IoT at the African Internet Summit 2019
# Released under GPL
#
from ledMatrix import matrix
import cayenne.client
import time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "CAYENNE_USERNAME"
MQTT_PASSWORD  = "CAYENNE_PASSWORD"
MQTT_CLIENT_ID = "CAYENNE_CLIENT_ID"

m = matrix.LedMatrix()
matrixChannel = 11

# switch the LED off, it is too bright!

m.clear()

# callback routine to treat command messages from Cayenne
def ledUpdate(message):

    msg = cayenne.client.CayenneMessage(message[0],message[1])
    if msg.channel != matrixChannel:
        return;
    level=int(msg.value);
    if level < 0 or level > 64:
        print("Illegal matrix value")
    m.setLevel(level)
    return

client = cayenne.client.CayenneMQTTClient(True)
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
# register callback
client.on_message=ledUpdate

client.loop_forever()


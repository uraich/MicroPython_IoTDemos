import cayenne.client
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "7c70a330-69af-11e8-a76a-fdebb8d0010d"
MQTT_PASSWORD  = "32d184add41570759dd1735fa464cef7e62876a4"
MQTT_CLIENT_ID = "d6accfc0-6541-11e9-bdb5-dfd20f02ea3f"


# The callback for when a message is received from Cayenne.
def on_message(message):
    print("message received: " + str(message))
    cmdMessage=cayenne.client.CayenneMessage(message[0],message[1])  # message[0]: topic, message[1]:payload
    print("Channel: %d"%cmdMessage.channel)
    print("value: %s"%cmdMessage.value)
    # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message

client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
#client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883, loglevel=logging.INFO)
client.loop_forever()


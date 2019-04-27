from cayenne import Cayenne

CLIENT_ID="CAYENNE_CLIENT_ID"
username='CAYENNE_USERNAME'
TOPIC_BASE = ("v1/%s/things/" % username)

def subscribeCayenne(clientID,channel):
  topic= TOPIC_BASE + clientID +'/cmd/%d'%channel
  print("Subscribing to topic %s, please wait 5 s"%topic)
  time.sleep(0.5)
  client.subscribe(topic)
  print("Subscribe sent")

def ledSwitch():
  print(topic,msg) 

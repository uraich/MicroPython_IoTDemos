from cayenne import Cayenne

CLIENT_ID="d6accfc0-6541-11e9-bdb5-dfd20f02ea3f"
username='7c70a330-69af-11e8-a76a-fdebb8d0010d'
TOPIC_BASE = ("v1/%s/things/" % username)

def subscribeCayenne(clientID,channel):
  topic= TOPIC_BASE + clientID +'/cmd/%d'%channel
  print("Subscribing to topic %s, please wait 5 s"%topic)
  time.sleep(0.5)
  client.subscribe(topic)
  print("Subscribe sent")

def ledSwitch():
  print(topic,msg) 

import paho.mqtt.client as mqtt  #import the client1
import time



def init():
	global client, subscriptions
	
	subscriptions = {}
	
	mqtt.Client.connected_flag=False#create flag in class
	broker=getConfig("broker") # To be developed
	client = mqtt.Client("python1")             #create new instance 
	client.loop_start()
	client.on_message = onMessage
	client.on_connect = onConnect
	
	print("Connecting to broker ",broker)
	client.connect(broker)      #connect to broker
	
	while client.connected_flag == False:
		pass
	
def subscribe(topic, callback):

	client.subscribe(topic)
	
	global subscriptions
	
	subscriptions[topic] = callback

	

def onMessage(client, userdata, msg):

	global test1
	global test2
	
	subscriptions[msg.topic](msg.payload)
	

def onConnect(client, userdata, flags, rc):
	client.connected_flag = True
	print ("CONNECTED")

def send(topic, value):
	global client
	
	if client.connected_flag == False:
		return False
    
	#print("sent")
	client.publish(topic, value)
	time.sleep(5)
    
	return True

def disconnect():
	global client
    
	client.loop_stop()    #Stop loop 
	client.disconnect() # disconnect
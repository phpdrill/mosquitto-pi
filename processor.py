import client
import temperature
import RPi.GPIO as GPIO

initPhase = None

def processNumber(thing):
	
	global initPhase
	
	if(thing["parameters"]["source"] == "temperature"):
		temp = temperature.read()
		res = client.send(thing["parameters"]["stateTopic"], str(temp))
		#print ("temperature " + str(temp) + " sent to " + thing["parameters"]["stateTopic"])
	

def processSwitch(thing):
	
	global initPhase
	
	if(initPhase == True):
		gpioNumber = int(thing["parameters"]["GPIO"])
	
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(gpioNumber, GPIO.OUT)
		
		def gotCommand(command):
			print "Switch got command " + command
		
			if(command == "ON"):
				GPIO.output(gpioNumber, GPIO.HIGH)
			
			if(command == "OFF"):
				GPIO.output(gpioNumber, GPIO.LOW)
						
		client.subscribe("home/outdoor/upper_valve", gotCommand)
		
		
		
	
def init():
	pass
	



def process(things):
	
	global initPhase
	
	initPhase = True
	
	#print ("Initializing")
	
	client.init()
	
	while True:
	
		for thing in things:
			
			if(thing["type"] == "number"):
				processNumber(thing)
				
			if(thing["type"] == "switch"):
				processSwitch(thing)
		
		# initPhase nach 1. Durchgang abgeschlossen.
		initPhase = False
		
def getCleanUpMethod():
	return cleanUp
	
def cleanUp():

	GPIO.cleanup() # cleanup all GPIO 
	client.disconnect()
	
	print("cleaned up")
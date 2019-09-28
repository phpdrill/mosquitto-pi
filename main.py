import time
import temperature
import things
import processor
import sys
import escape

print ("main ok")

cleanUpMethod = processor.getCleanUpMethod()

try:
	
	things = things.load()
	
	processor.init()
	
	processor.process(things)
	
		
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	print("Keyboard interrupt")

except Exception, e:
	print(escape.FAIL + str(e) + escape.ENDC) 

finally:
	cleanUpMethod()



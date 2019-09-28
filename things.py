import os

TYPE_KEY = "Type "
PARAMETER_START_KEY = "["
PARAMETER_END_KEY   = "]"

def load():
	
	print ("a1")
	things = []
	
	thingsFilePath = os.path.dirname(__file__) + "/things.things"
	
	thingsFile = open(thingsFilePath, "r")
	
	thingsLines = thingsFile.readlines()
	
	for thingsLine in thingsLines:
	
		things.append(parse(thingsLine))
	
	return things

def parse(thingsLine):
	
	# Type
	typeKeyPosition = thingsLine.find(TYPE_KEY)
	if(typeKeyPosition == -1):
		raise Exception("Error in things.things: " + TYPE_KEY + " not found.")
	
	typeValueStartPosition = typeKeyPosition + len(TYPE_KEY)
	typeValueEndPosition   = thingsLine.find(" ", typeValueStartPosition)
	if(typeValueEndPosition == -1):
		raise Exception("Error in things.things: After " + TYPE_KEY + ", there is no ' '.")
	
	type = thingsLine[typeValueStartPosition:typeValueEndPosition]
	
	# Parameters
	parameterStartPosition = thingsLine.find(PARAMETER_START_KEY, typeValueEndPosition)
	if(parameterStartPosition == -1):
		raise Exception("Error in things.things: " + PARAMETER_START_KEY + " not found.")
	parameterStartPosition += 1
		
	parameterEndPosition = thingsLine.find(PARAMETER_END_KEY, typeValueEndPosition)
	if(parameterEndPosition == -1):
		raise Exception("Error in things.things: " + PARAMETER_END_KEY + " not found.")
	
	parameterString = thingsLine[parameterStartPosition :parameterEndPosition]
	
	parameters = parameterString.split(",")
	
	parameterDictionary = {}
	
	for parameter in parameters:
		parameter = parameter.strip()
		
		parameterParts = parameter.split("=")
		parameterKey   = parameterParts[0]
		parameterValue = parameterParts[1].strip('"')
		
		parameterDictionary[parameterKey] = parameterValue
		
	return {"type": type, "parameters": parameterDictionary}
	
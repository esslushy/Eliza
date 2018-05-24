import re
import reference
import random


	

def matchPPatterns(response):
	for i in reference.psychobabble_patterns:
		match  = re.match(reference.psychobabble_patterns[i], response)
		if(not (match is None)):
			return i
def respond(pPatterns):
	x = reference.psychobabble_responses[pPatterns][random.randrange(len(reference.psychobabble_responses[pPatterns]))]
	return x

def format(matchDictKey, elizaResponse, response):
	match = re.match(reference.psychobabble_patterns[matchDictKey], response)
	return reference.format_response(match, elizaResponse)


response = input("Hello, how are you today?\n")
response = re.sub(".!", "", response.lower())
elizaResponse = format(matchPPatterns(response), respond(matchPPatterns(response)), response)
if(response == "quit"):
	print(elizaResponse)
while(not response == "quit"):
	response = input(elizaResponse + "\n")
	response = re.sub(".!", "", response.lower())
	elizaResponse = format(matchPPatterns(response), respond(matchPPatterns(response)), response)
	if(response == "quit"):
		print(elizaResponse)
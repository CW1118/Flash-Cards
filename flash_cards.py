import random
import speech_recognition as sr
import pyaudio

material = {"not False": "True",
"not True": "False",
"True or False": "True",
"True or True": "True",
"False or True": "True",
"False or False": "False",
"True and False": "False",
"True and True": "True",
"False and True": "False",
"False and False": "False",
"not (True or False)": "False",
"not (True or True)": "False",
"not (False or True)": "False",
"not (False or False)": "True",
"not (True and True)": "False",
"not (False and True)": "True",
"not (False and False )": "True",
"1 != 0": "True",
"1 != 1": "False",
"0 != 1": "True",
"0 != 0": "False",
"1 == 0": "False",
"1 == 1": "True",
"0 == 1": "False",
"0 == 0": "True"}

choice = raw_input("Do you want to study using 'text' or 'voice'?"

while True:
	if choice == "text":
		text()
		
	elif choice == "voice":
		audio()
		
	else:
		print "I don't understand.  Try typing 'text' or 'voice'."
		
def audio():
	#***STILL IN TESTING***
	r = sr.Recognizer()
	
	with sr.Microphone() as source:                # use the default microphone as the audio source
		audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

	try:
		print("You said " + r.recognize(audio))   		# recognize speech using Google Speech Recognition
	
	except LookupError:                            # speech is unintelligible
		print("Could not understand audio")

def text():
	
	while True:
		question = random.choice(material.keys())
		answer = material[question]
		
		print question
		ans = raw_input("> ")
		
		if ans == "t":
			ans = "True"
			break
					
		elif ans == "f":
			ans = "False"
			break
			
		else:
			print "Please type 't' for True or 'f' for False"
				
	if ans == answer:
		print "CORRECT, %r is %s.\n" % (question, answer)
		
	else:
		print "WRONG, %r is %s.\n" % (question, answer)
		
	text()

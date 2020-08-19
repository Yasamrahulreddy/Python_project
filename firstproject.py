import os
import subprocess
import pyttsx3
pyttsx3.speak("Hey Rahul iam your virtual assistent")

pyttsx3.speak("What are you looking for?")
while True:
	print("What are you looking for ? "  , end='')
	p = input()

	if  (("run" in p) or ("open" in p))  and ("chrome" in p):
		pyttsx3.speak("opening chrome")
		os.system("chrome")
		pyttsx3.speak("closing chrome")
		
		
	elif (("run" in p) or  ("open" in p )) and  (("notepad" in p) or ("editor" in p) ) :		
		pyttsx3.speak("opening notepad")
		os.system("notepad")
		pyttsx3.speak("closing notepad")

	elif (("run" in p) or  ("open" in p )) and ("windows" in p) and ("mediaplayer" in p) :
		  pyttsx3.speak("opening windows mediaplayer")
		  os.system("wmplayer")
		  pyttsx3.speak("closing windows mediaplayer")
		
	    
	
	elif (("run" in p) or("open" in p ))and ("firefox" in p) :
		pyttsx3.speak("opening firefox")
		os.system("firefox")
		pyttsx3.speak("closing firefox")
		


	elif (("run" in p) or ("open" in p ))and ("notes" in p) :
		pyttsx3.speak("opening stickynotes")
		os.system("StikyNot")
		pyttsx3.speak("closing stickynotes")

	elif  (("run" in p) or("open" in p ))and ("defender" in p) :
		pyttsx3.speak("opening windows defender")
		subprocess.call(['C:\Program Files\Windows Defender\MSASCui.exe'])
		pyttsx3.speak("closing windows defender")


	elif (("run" in p) or("open" in p ))and ("reader" in p) :
		pyttsx3.speak("opening adobe reader")
		subprocess.call(['C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'])
		pyttsx3.speak("closing adobe reader")

	elif  (("run" in p) or("open" in p ))and ("atom" in p) :
		pyttsx3.speak("opening atom")
		os.system("Atom")
		pyttsx3.speak("closing atom")

	elif (("run" in p) or("open" in p ))and ("vs code" in p) :
		pyttsx3.speak("opening Visual Studio Code")
		os.system('code')
		pyttsx3.speak("closing Visual Studio Code")


	elif ("open" in p )and ("paint" in p) :
		pyttsx3.speak("opening paint")
		os.system('mspaint')
		pyttsx3.speak("closing paint")
	  
	elif ("open" in p )and ("snipper" in p) :
		pyttsx3.speak("opening SnippingTool")
		os.system('SnippingTool')  
		pyttsx3.speak("closing SnippingTool")

	elif("open" in p) and ("recorder" in p):
		pyttsx3.speak("opening recorder")
		os.system('psr')
		pyttsx3.speak("closing recorder")

	elif("open" in p) and ("remote desktop" in p):
		pyttsx3.speak("opening remote desktop")
		os.system('mstsc')
		pyttsx3.speak("closing remote desktop")

	elif("open" in p) and ("system" in p) and("information" in p) or ("info" in p):
		pyttsx3.speak("opening system information")
		os.system('msinfo32')
		pyttsx3.speak("closing system information")

	elif("open" in p) and ("task manager" in p):
		pyttsx3.speak("opening task manager")
		os.system('Taskmgr')
		pyttsx3.speak("closing task manager")

	elif("open" in p) and ("vlc" in p) and ("mediaplayer" in p ):
		pyttsx3.speak("opening vlc media player")
		os.system('vlc')
		pyttsx3.speak("closing vlc media player")	
	
	elif  ("exit" in p)  or ("quit" in p) or ("close" in p):
		pyttsx3.speak("Byeee !Thank You Have a nice day ")
		print("Byeee !Thank You Have a nice day ")
		break

	else:
		pyttsx3.speak("doesn't support ")
		print("doesn't support")


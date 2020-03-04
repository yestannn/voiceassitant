import  speech_recognition as sr  
import playsound # to play saved mp3  
from gtts import gTTS # google text to speech 
from selenium import webdriver
import os  


num = 1
def assistant_speaks(output): 
	global num 
  
	# num to rename every audio file  
	# with different name to remove ambiguity 
	num += 1
	print("Aya: ", output) 
  
	toSpeak = gTTS(text = output, lang ='en', slow = False) 
	# saving the audio file given by google text to speech 
	file = str(num)+".mp3"
	toSpeak.save(file) 
	  
	# playsound package is used to play the same file. 
	playsound.playsound(file, True)  
	os.remove(file)

def get_audio(): 
  
	rObject = sr.Recognizer() 
	audio = '' 
  
	with sr.Microphone() as source: 
		print("Speak...") 
		  
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5)  
	print("Stop.") # limit 5 secs 
  
	try: 
  
		text = rObject.recognize_google(audio, language ='en-US') 
		print("You : ", text) 
		return text 
  
	except: 
  
		return 0

def text_search(text):
	if "hello" in text.lower() or "hi" in text.lower() :
		assistant_speaks("Hi")
		return
	elif "what can you do" in text.lower() :
		assistant_speaks("I can open you Chrome talk with, search in internet")
		return
	elif "stop" in text.lower() or "bye" in text.lower() or "see you later" in text.lower():
		assistant_speaks("See you later")
		return
	elif "how are you " in text.lower() or "how you doing" in text.lower() :
		assistant_speaks("I'm fine")
		return

	elif  "who made you" in text.lower() or "who created you" in text.lower() :
		assistant_speaks("I was created by Astana IT University Students")
		return
	elif "search in web" in text.lower() or "search" in text.lower()  or "google about" in text.lower() :
		assistant_speaks("wait a moment")
		search_web()
		return
	else:
		assistant_speaks("I don't understand you")
		return


def search_web(): 
  
	chromedriver = r'C:\Users\skhanseiit\Desktop\pyvoise\chromedriver.exe'
	driver = webdriver.Chrome(chromedriver)
	assistant_speaks("please say what you want")
	text = get_audio()

  
	if 'youtube' in text.lower(): 
  
		assistant_speaks("Opening in youtube") 
		 
		driver.get("http://www.youtube.com") 
		return
  
	elif 'wikipedia' in text.lower(): 
  
		assistant_speaks("Opening Wikipedia") 
		
		driver.get("https://en.wikipedia.org")
		return
  
	else: 
  
		if 'open google' in text: 
  
			indx = input.lower().split().index('google') 
			
			driver.get("https://www.google.com")
  
		elif 'search' in input: 
  
			indx = text.lower().split().index('google') 
			query = text.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
		else: 
  
			driver.get("https://www.google.com/search?q =" + '+'.join(text.split())) 
  
		return



if __name__ == "__main__": 

	while (True):
		text = get_audio()
		
		if text == 0:
			assistant_speaks("please, repeat")
		else:
			text_search(text)


# Converting Audio in Text

#Importing Libraries

import speech_recognition as sr
import pyaudio

#Converting Our Speech into text
r = sr.Recognizer()
with sr.Microphone() as source:
  print("Speak anything : ")
  audio = r.listen(source)
  try:
    text = r.recognize_google(audio)
    print("Say Something: {}".format(text))
  except:
    print("sorry")
    
    
#Converting wav file into text
df =   'audio.wav'
r = sr.Recognizer()
with sr.AudioFile(df) as source:
  #print("Speak anything : ")
  audio = r.record(source)
  try: 
   print("The audio file contains: " + r.recognize_google(audio)) 
  
  except sr.UnknownValueError: 
   print("Google Speech Recognition could not understand audio") 
  
  except sr.RequestError as e: 
   print("Could not request results from Google Speech Recognition service; {0}".format(e))
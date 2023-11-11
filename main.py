import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess 
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import openai
import random
import imdb


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
   engine.say(text)
   engine.runAndWait()





def wishMe():
   hour=datetime.datetime.now().hour
   if hour>=0 and hour<12:
     message = "Hello,Good Morning Sir"
     speak(message)
     print(message)
   elif hour>=12 and hour<18:
     message = "Hello,Good Afternoon Sir"
     speak(message)
     print(message)
   else:
      message = "Hello,Good Evening Sir"
      speak(message)
      print(message)




def takeCommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening...")
      audio=r.listen(source)
   
   try: 
      statement=r.recognize_google(audio,language='en-in')
      print(f"user said:{statement}\n")
      
   except Exception as e:
      speak("Pardon me, please say that again")
      return "None"
   return statement

print("Loading your AI personal assistant Jarvis")
speak("Loading your AI personal assistant Jarvis")
wishMe()



if __name__=='__main__':
   
   while True:
      speak("Tell me how can I help you now?")
      statement = takeCommand().lower()
      if statement==0:
         continue



      if "good bye" in statement or "ok bye" in statement or "stop" in statement:
         speak('Your personal assistant Jarvis is shutting down, Bye, talk you later...')
         print('Your personal assistant Jarvis is shutting down, Bye, talk you later...')
         break


      if 'wikipedia' in statement:
         speak('Searching Wikipedia...')
         statement =statement.replace("wikipedia", "")
         results = wikipedia.summary(statement, sentences=4)
         speak("According to Wikipedia")
         print(results)
         speak(results)




      elif 'open youtube' in statement:
         webbrowser.open_new_tab("https://www.youtube.com")
         speak("youtube is opening now")
         time.sleep(5)
   
      elif 'open google' in statement:
         webbrowser.open_new_tab("https://www.google.com")
         speak("Google chrome is opening now")
         time.sleep(5)

      elif 'open gmail' in statement:
         webbrowser.open_new_tab("gmail.com")
         speak("GMail opening now")
         time.sleep(5)

      #elif 'how is the movie' in statement:
      #   speak('Searching Wikipedia...')
      #   statement=statement.replace("wikipedia", "")
      #   results= wikipedia.summary(statement, sentences=4)
      #   speak("According to Wikipedia")
      #   print(results)
      #   speak(results)

      elif 'how is the movie' in statement:
         speak('Searching on IMDB...')
         statement=statement.replace("imdb", "")
         results= imdb.IMDb().search_movie(statement, sentence=4)
         speak("According to IMDB")
         print(results)
         speak(results)
         for i in results:
            print(i)




      elif 'time' in statement:
         strTime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"the time is {strTime}")



      elif 'news' in statement:
         news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
         speak('Here are some headlines from the Times of India,Happy reading')
         time.sleep(6)

      elif "camera" in statement or "take a photo" in statement:
         ec.capture(0,"robo camera","img.jpg")

      elif 'search' in statement:
         statement = statement.replace("search", "")
         webbrowser.open_new_tab(statement)
         time.sleep(5)




      elif 'who are you' in statement or 'what can you do' in statement:
         speak('Hello User, I am Jarvis your personal assistant. I have been built by Master Piyangshu Banik to perform minor tasks like'
          'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
          'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


      elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
         speak("I was built by Master Piyangshu Banik")
         print("I was built by Master Piyangshu Banik")
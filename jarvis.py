import time
import kit as kit
import sys
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import pyaudio
import pyglet
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import secure_smtplib
import smtplib
import spotipy
import  json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices' , voices[0].id)

# method to change text to audio
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold =1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
        try:
            print("Recognizing...")
            query =  r.recognize_google(audio , language='en-in')
            print(f"User said: {query} ")
        except Exception as e:
            speak("Say that again please...")
            return "none"
        return query

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0  and hour <= 12:
        speak("Good Moring Abdul Razaque")
    elif hour > 11 and hour < 18:
        speak("Good Afternoon Abdul Razaque")
    else:
        speak("Good Evening Abdul Razaque")
    speak("Razaque I am Jarvis, plaease tell me how can i help you")

# to send EMail
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your passwor')
    server.sendmail('your email id', to,content)
    server.close()

if __name__  ==  "__main__":
    wish()
    while True:
    # if 1:
        query = takecommand().lower()
        #     logic building for tasks
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open google chrome" in query:
            speak("Razaque what should i search on google chrome")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "open intellij idea" in query:
            npath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.2\\bin\\idea64.exe"
            os.startfile(npath)
        elif "open pycharm" in query:
            npath = "C:\\Python\\PyCharm Community Edition 2022.1\\bin\\pycharm64.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
                cap.release()
                cv2.destroyAllWindows()
        elif "open music" in query:
            music_dir = "D:\\CARUSB"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get('https://api.apify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open('www.youtube.com')
        elif "open facebook" in query:
            webbrowser.open('www.facebook.com')
        elif "open instagram" in query:
            webbrowser.open('www.instagram.com')
        elif "open stack overflow" in query:
            webbrowser.open('www.stackoverflow.com')
        # elif "send message" in query:
        #     pywhatkit.sendwhatmsg("+923018989066","Jani Kaaaly angorr ?",20,22)
        elif "play song on youtube" in query:
            pywhatkit.playonyt("No Love")
        elif "email to Suresh" in query:
            try:
                speak("What should i say ")
                content = takecommand().lower()
                to = "suresh.bscsses21@iba-suk.edu.pk"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Razaque I can't sent Email ")
        elif "close notepad" in query:
            speak("Ok Razaque    closing Notepad")
            os.system("taskkill /f /im notepad.exe ")
        elif "no thanks" in query:
            speak("thanks for using me Razaque, have a good day")
            sys.exit()
        speak("Razaque do you have another work that may I help you")
    #     to close any application










    # takecommand()
    # speak("Good Evening  Abdul Razaque Goraya")

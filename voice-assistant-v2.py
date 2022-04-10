# Voice Assistant v2.0
# Created by Gabriel Tavares

import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from time import ctime
import webbrowser
import ssl
import certifi
import time
import os


# initialize a recognizer
r = sr.Recognizer()
# listen for audio and convert it to text
def record_audio (ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source) # listen for audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio) # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('Sorry, I did not get that')
        except sr.RequestError: # error: Recognizer is not connected
            speak('Sorry, my service is down')
        print("f >> {voice_data.lower()}") # print what user said
        return voice_data.lower()
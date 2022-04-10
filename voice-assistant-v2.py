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


# make the AI recognize the user
class person:
    name = ''
    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


# initialize a recognizer
r = sr.Recognizer()


# listen for audio and convert it to text
def record_audio(ask=False):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            speak('Sorry, I did not get that')
        except sr.RequestError:  # error: Recognizer is not connected
            speak('Sorry, my service is down')
        print("f >> {voice_data.lower()}")  # print what user said
        return voice_data.lower()


# reply to the question
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  # text to speach(voice) in english
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save audio as .mp3
    playsound.playsound(audio_file)  # play the audio file
    print(f"May Day: {audio_file}")  # print what the app said
    os.remove(audio_file)  # remove audio file

# Voice Assistant Test environment

import speech_recognition as sr
import playsound
import pyaudio
from gtts import gTTS
import random
import os
import time
import datetime

class person:
    name = ''

    def setName(selfself, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            r.adjust_for_ambient_noise(source)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
            print('Sorry I did not get that')
        except sr.RequestError:
            speak('Sorry, my service is down')
            print('Sorry, my service is down')
        print(f">> {voice_data.lower()}")
        return voice_data.lower()


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(f"May Day: {audio_file}")
    os.remove(audio_file)


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def respond(voice_data):
    greeting()
    speak('How can I help you?')

    if there_exists(['hey', 'hi', 'hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
                     f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}",
                     f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)

    if there_exists(['what is your name', 'what is your name', 'tell me your name']):
        if person_obj.name:
            speak('My name is Aaliyah')
        else:
            speak('My name is Aaliyah, What is your name?')

    if there_exists(['My name is', 'I am']):
        person_name = voice_data.split('is')[-1].strip()
        speak(f'okay, I will remember that {person_name}')
        person_obj.setName(person_name)

    if there_exists(['how are you', 'how you feeling']):
        speak(f'I am very well, thanks for asking {person_obj.name}')

    if there_exists(['exit', 'quit', 'goodbye']):
        speak('going offline')
        exit()


time.sleep(1)

person_obj = person()
while(1):
    voice_data = record_audio()
    respond(voice_data)

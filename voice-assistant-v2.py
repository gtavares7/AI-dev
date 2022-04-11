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


# get string and make an audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  # text to speach(voice) in english
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save audio as .mp3
    playsound.playsound(audio_file)  # play the audio file
    print(f"May Day: {audio_file}")  # print what the app said
    os.remove(audio_file)  # remove audio file

# how to respond to the question
def respond(voice_data):
    speak('How can I help you?')

    # 1: Greeting
    if there_exists(['hey', 'hi', 'hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
                     f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}",
                     f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)

    # 2: Name
    if there_exists(['what is your name', 'what is your name', 'tell me your name']):
        if person_obj.name:
            speak('My name is Aaliyah')
        else:
            speak('My name is Aaliyah. What is your name?')

    # function to remember user's name
    if there_exists(['My name is', 'I am']):
        person_name = voice_data.split('is')[-1].strip()
        speak(f'okay, I will remember that {person_name}')
        person_obj.setName(person_name)  # remember name is person object

    # 3: Greeting
    if there_exists(['how are you','how are you doing']):
        speak(f'I am very well, thanks for asking {person_obj.name}')

    # time
    if there_exists(['what time is it','tell me the time','can I have the time']):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hour = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # Search Google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on Google')

    # Search YouTube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on YouTube')
        




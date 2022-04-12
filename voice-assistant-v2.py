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
import datetime
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


# Time-dependent greeting function
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")

# how to respond to the question
def respond(voice_data):
    greeting()
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
    if there_exists(['how are you', 'how are you doing']):
        speak(f'I am very well, thanks for asking {person_obj.name}')

    # 4: who am I
    if there_exists(['who are you', 'who made you']):
        speak('My name is Aaliyah. I am an AI voice assistant created by Gabriel Tavares.')

    if there_exists(['what can you do', 'what are your capabilities']):
        speak('I can complete small tasks such as opening a web browser, playing music,'
              'providing the date and time as well as weather conditions in any city.'
              'I can also complete complex computational equations.')

    # 5: Time
    if there_exists(['what time is it', 'tell me the time', 'can I have the time']):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hour = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # 6: Search Google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on Google')

    # 7: Open Gmail
    if there_exists(['open gmail', 'open my mail', 'show me my mail']):
        webbrowser.open_new_tab('https://mail.google.com')
        speak('Opening Gmail')

    # 8: Search YouTube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on YouTube')

    # 9: Play music
    if there_exists(['play']):
        search_term = voice_data.split("play")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak('Playing' + {search_term})

    # 10: Open the News
    if there_exists(['show me the news', 'open the news', 'what is the latest news']):
        webbrowser.open_new_tab('https://news.google.com/foryou')

    # 11: Get stock price
    if there_exists(['price of']):
        # strip removes whitespace before/after a term in string
        search_term = voice_data.lower().split(" of ")[-1].strip()
        stocks = {
            "apple": "AAPL",
            "microsoft": "MSFT",
            "facebook": "FB",
            "tesla": "TSLA",
            "bitcoin": "BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]

            speak(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
        except:
            speak('oops, something went wrong')
    if there_exists(['exit', 'quit', 'goodbye']):
        speak('going offline')
        exit()


time.sleep(1)

person_obj = person()
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond



# Aaliyah AI
# Created by Gabriel Tavares

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)
# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume+25)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        talk("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        talk("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        talk("Hello,Good Evening")
        print("Hello,Good Evening")


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'aaliyah' in command:
                command = command.replace('aaliyah', '')
                print(command)
    except:
        pass
    return command


greeting()


def run_aaliyah():
    talk('How can I help you?')
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        print('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)

    elif 'wikipedia' in command:
        talk('Searching Wikipedia...')
        print('Searching Wikipedia...')
        command = command.replace('wikipedia', '')
        results = wikipedia.summary(command, 3)
        talk('According to Wikipedia')
        talk(results)
        print(results)

    elif 'date with me' in command:
        talk("I don't think you're my type")
        print("I don't think you're my type")

    elif 'that hurt my feelings' in command:
        talk('suck it up, buttercup!')
        print('suck it up, buttercup!')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    else:
        talk('Please say that again')
        print('Please say that again')


while True:
    try:
        run_aaliyah()
    except UnboundLocalError:
        print('No command detected! Aaliyah is shutting down!')
        break

# Aaliyah AI
# Created by Gabriel Tavares

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser

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

    if 'who are you' in command:
        talk('My name is Aaliyah. I am an AI voice assistant created by Gabriel Tavares.'
             'My physical self was created by my mommy Fanta.')

    elif 'what can you do' in command:
        talk('I can complete small tasks such as opening a web browser, playing music,'
             'providing the date and time as well as weather conditions in any city.'
             'I can also complete complex computational equations.')

    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        print('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'search' in command:
        search = command.replace('search', '')
        talk('looking up' + search)
        pywhatkit.info(search, lines=4)

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

    elif 'open google' in command:
        webbrowser.open_new_tab('https://www.google.ca')
        talk('Google chrome is now opened')

    elif 'open gmail' in command:
        webbrowser.open_new_tab('https://mail.google.com')
        talk('Gmail is now opened')

    elif 'open youtube' in command:
        webbrowser.open_new_tab('https://www.youtube.com')
        talk('Youtube is now opened')

    elif 'date with me' in command:
        talk("I don't think you're my type")
    elif 'that hurt my feelings' in command:
        talk('suck it up, buttercup!')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif "power off" in command or "shut down" in command:
        talk("Ok , your pc will shut down in 10 seconds")
        subprocess.call(["shutdown", "/l"])

    else:
        talk('Please say that again')


while True:
    try:
        run_aaliyah()
    except UnboundLocalError:
        print('No command detected! Aaliyah is shutting down!')
        break

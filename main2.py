#!/usr/local/bin/python3.9
# -*- coding: utf-8 -*-

# AI Test
# Created by Gabriel Tavares

# package needed to process speech recognition
import speech_recognition as sr
# package needed to make the AI speak back to the user
import pyttsx3
# package group that includes a bunch of other packages
import pywhatkit
# built-in package for Date and Time
import datetime
# package for time.sleep
import time
# package for wikipedia searches
import wikipedia
# package to have AI tell a joke
import pyjokes
# package to control OS applications
# import os
# package to open WebBrowser
import webbrowser
# package for weather reports
# import requests

# create a listener for SpeechRecognition, sr.Recognizer() is used to recognize my voice
listener = sr.Recognizer()
# engine that will speak back to me
engine = pyttsx3.init()
# declare variable of voices to get all provided voices in pyttsx3
voices = engine.getProperty('voices')
# tell engine to set voices to voice index 0
engine.setProperty('voice', voices[0].id)


# define function to  say whatever parameter we pass to the function
def talk(text):
    engine.say(text)
    engine.runAndWait()


# function to make AI greet me depending on the time of day
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
        time.sleep(2)


# define function to take inputs as commands
def take_command():
    # Try block to check for errors
    try:
        # use microphone as source of audio
        with sr.Microphone() as source:
            print('listening...')
            # declare Voice variable to listen to our source
            voice = listener.listen(source)
            # once we have the source, use Google to convert the voice variable input into text
            command = listener.recognize_google(voice)
            # send command to lowercase
            command = command.lower()
            # check if 'alexa' is mentioned in the command, if not then quit
            if 'aaliyah' in command:
                # remove the word alexa from the input string
                command = command.replace('aaliyah', '')
                print(command)
    except:
        pass
    return command


# make AI greet me
greeting()


# function to run AI
def run_aaliyah():
    talk('How can I help you?')
    # take output from take_command() and use it as input in run_aaliyah()
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
        # remove 'play' from input string
        song = command.replace('play', '')
        talk('Playing ' + song)
        # function to play song on YouTube
        pywhatkit.playonyt(song)

    # google search
    elif 'search' in command or 'look up' in command:
        search = command.replace('search', '')
        talk('looking up ' + search)
        pywhatkit.info(search)

    # function to get time
    elif 'time' in command:
        # call datetime "now()" and set string format time to Hours:Minutes AM/PM
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)

    # function to search the wikipedia database
    elif 'wikipedia' in command:
        talk('Searching Wikipedia...')
        # remove 'wikipedia' from input string
        command = command.replace('wikipedia', '')
        # pass 'command' output in summary method and show 3 lines
        results = wikipedia.summary(command, 3)
        # output Wikipedia results
        talk('According to Wikipedia')
        print(results)
        talk(results)

    # function to open google.ca in web browser
    elif 'open google' in command:
        webbrowser.open_new_tab("https://www.google.ca")
        talk('Google chrome is now opened')

    # open YouTube in a web browser
    elif 'open youtube' in command:
        webbrowser.open_new_tab("https://www.youtube.com")
        talk('Youtube is now opened')

    # open GMail
    elif 'open gmail' in command:
        webbrowser.open_new_tab('https://mail.google.com')
        talk('Gmail is now opened')

    # function to ask aaliyah on a date
    elif 'date with me' in command:
        talk("I don't think you're my type")
    elif 'that hurt my feelings' in command:
        talk('suck it up, buttercup!')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    # function set in case AI does not understand input
    else:
        talk('Please say that again')


# Runs Aaliyah AI in a loop
while True:
    try:
        run_aaliyah()
    except UnboundLocalError:
        print("No command detected! Aaliyah is shutting down! ")
        break

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
# package for wikipedia searches
import wikipedia
# package to have AI tell a joke
import pyjokes

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


# function to run AI
def run_aaliyah():
    # take output from take_command() and use it as input in run_aaliyah()
    command = take_command()
    print(command)
    if 'play' in command:
        # remove 'play' from input string
        song = command.replace('play', '')
        talk('playing' + song)
        # function to play song on YouTube
        pywhatkit.playonyt(song)

    # function to get time
    elif 'time' in command:
        # call datetime "now()" and set string format time to Hours:Minutes AM/PM
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)

    # function to search the wikipedia database
    elif 'wikipedia' in command:
        speak('Searching Wikipedia...')
        # remove 'wikipedia' from input string
        command = command.replace("wikipedia", "")
        # pass 'command' output in summary method and show 3 lines
        results = wikipedia.summary(command, sentences=3)
        # output Wikipedia results
        speak("According to Wikipedia")
        print(results)
        speak(results)

    # function to ask aaliyah on a date
    elif 'date with me' in command:
        talk("I don't think you're my type")
    elif 'that hurt my feelings' in command:
        talk('suck it up, buttercup!')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    

run_aaliyah()

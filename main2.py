#!/usr/local/bin/python3.9
# -*- coding: utf-8 -*-

# AI Test
# Created by Gabriel Tavares

# package needed to process speech recognition
import speech_recognition as sr
# package needed to make the AI speak back to the user
import pyttsx3

# create a listener for SpeechRecognition, sr.Recognizer() is used to recognize my voice
listener = sr.Recognizer()
# engine that will speak back to me
engine = pyttsx3.init()
# declare variable to control the speed of the AI voice
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-70)
# declare variable to control the volume of the AI voice
# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume+0.25)
# declare variable of voices to get all provided voices
voices = engine.getProperty('voices')
# tell engine to set voices to voice index 1
engine.setProperty('voice', voices[1].id)
engine.say('Hello, I am your AI prototype')
engine.say('What can I do for you?')
engine.runAndWait()

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
        if 'alexa' in command:
            #engine.say(command)
            #engine.runAndWait()
            print(command)
except:
    pass
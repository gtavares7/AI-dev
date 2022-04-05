#!/usr/local/bin/python3.9
# -*- coding: utf-8 -*-

import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


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
    return

def run_aaliyah():
    command = take_command()
    print(command)
    if 'play' in command:
        talk('playing song...')
        print('playing song...')


run_aaliyah()
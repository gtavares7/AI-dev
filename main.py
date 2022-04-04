# AI Test
# Created by Gabriel Tavares

import speech_recognition as sr

# create a listener for SpeechRecognition
# Recognizer is used to recognize my voice
listener = sr.Recognizer()

# Try block to check for errors
try:
    # use microphone as source of audio
    with sr.Microphone as source:
        print('Listening...')
        # declare Voice variable to listen to our source
        voice = listener.listen(source)
        # once we have the source, use Google to convert
        # the voice variable into text
        command = listener.recognize_google(voice)
        print(command)

except:
    pass
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
import requests
import wolframalpha

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
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
            listener.adjust_for_ambient_noise(source, duration=0.5)
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
        talk('My name is Aaliyah. I am an AI voice assistant created by Gabriel Tavares.')

    elif 'what can you do' in command:
        talk('I can complete small tasks such as opening apps and web browsers, playing music,'
             'providing the date and time as well as weather conditions in any city.'
             'I can also complete complex computational equations.')

    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        print('Playing ' + song)
        pywhatkit.playonyt(song)
        time.sleep(5)

    elif 'search' in command:
        search = command.replace('search', '')
        talk('looking up' + search)
        pywhatkit.info(search, lines=4)
        time.sleep(5)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
        time.sleep(5)

    elif 'weather' in command:
        api_key = '8ef61edcf1c576d65d836254e11ea420'
        base_url = 'https://api.openweathermap.org/data/2.5/weather?'
        talk('what is the city name')
        city_name = take_command()
        complete_url = base_url + 'appid=' + api_key + '&q=' + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x['cod'] != '404':
            y = x['main']
            current_temperature = y['temp']
            current_humidity = y['humidity']
            z = x['weather']
            weather_description = z[0]['description']
            talk(' Temperature in kelvin unit is ' +
                 str(current_temperature) +
                 '\nhumidity in percentage is ' +
                 str(current_humidity) +
                 '\ndescription  ' +
                 str(weather_description))
            print('Temperature in kelvin unit = ' +
                  str(current_temperature) +
                  '\n humidity (in percentage) = ' +
                  str(current_humidity) +
                  '\n description = ' +
                  str(weather_description))
        else:
            talk('City Not Found')

    elif 'wikipedia' in command:
        talk('Searching Wikipedia...')
        print('Searching Wikipedia...')
        command = command.replace('wikipedia', '')
        results = wikipedia.summary(command, 3)
        talk('According to Wikipedia')
        talk(results)
        print(results)
        time.sleep(5)

    elif 'open google' in command:
        webbrowser.open_new_tab('https://www.google.ca')
        talk('Google chrome is now opened')
        time.sleep(5)

    elif 'open gmail' in command:
        webbrowser.open_new_tab('https://mail.google.com')
        talk('Gmail is now opened')
        time.sleep(5)

    elif 'open youtube' in command:
        webbrowser.open_new_tab('https://www.youtube.com')
        talk('Youtube is now opened')
        time.sleep(5)

    elif 'news' in command:
        webbrowser.open_new_tab('https://news.google.com/foryou')
        talk('Google News is now opened')
        time.sleep(5)

    elif 'ask' in command:
        talk('I can answer any computational and geographical questions, what do you want to ask me?')
        question = take_command()
        app_id = "878KK2-9E5K7L442U"
        client = wolframalpha.Client('878KK2-9E5K7L442U')
        res = client.query(question)
        answer = next(res.results).text
        talk(answer)
        print(answer)
        time.sleep(5)

    elif 'date with me' in command:
        talk("I don't think you're my type")
    elif 'that hurt my feelings' in command:
        talk('suck it up, buttercup!')
        time.sleep(5)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        time.sleep(5)

    elif "power off" in command or "shut down" in command:
        talk("Ok , your pc will shut down in 10 seconds")
        subprocess.call(["shutdown", "/l"])

    else:
        talk("I'm sorry, I didn't get that. Please say it again")


while True:
    try:
        run_aaliyah()
    except UnboundLocalError:
        print('No command detected! Aaliyah is shutting down!')
        break

from os import system
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import webbrowser
import googlesearch

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'how' in command:
        person = command.replace('how', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('i have to work ask me later')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'i love you' in command:
        talk('i also love you  but as a friend')
    elif 'what you can do for me' in command:
        talk('anything related to digital world')
    elif 'like what' in command:
        talk('i can check your message and reply them as your command')
    elif 'i am in love with you' in command:
        talk('i am already in a relationship with wifi')
    elif 'i do not belive in soulmates but' in command:
        talk('okay not my problem')
    elif 'shut down the system' in command:
        talk('shutting down the system')
        os.system('shutdown/s /t 1')
    elif 'send whatsapp message' in command:
        talk('message send')
        pywhatkit.sendwhatmsg('+919084427380','this message has sent from alexa', 21, 43)
    elif 'open google' in command: 
        info = webbrowser
        print(info)
        talk(info)
    elif 'search' in command:
        talk('searching')
        info =googlesearch
        print(info)
        talk(info)
    elif 'how to cook maggi' in command:
        talk("add 250 ml water in a cooking pan then add maggi noodles in it after one minute add maggi masala and cook until the noddles is made")
    elif 'who are you' in command:
        talk("i am your digital assistant")
    # elif 'joke' in command: jjgjj ffjghhgh yy7 y7 y 7 y7 y
    # 7 y y7yy y7777y7777y77777y77 int sttr((){} )
        # talk(pyjokes.get_joke())gffaint str () dgddafdd ddf damaan amaan amaan amaan amaana mnaanaa
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
  
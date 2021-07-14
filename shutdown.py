# import required modules 
import os
from pyttsx3 import engine
import speech_recognition as sr
import pyttsx3
#  create class
class amaancode:
    # method to take input 
    def takeCommands(self):
        #  using microphone for input voice
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            # number of seconds of non-speaking audio before
            # a phrase is completed 
            r.pause_threshold =1
            audio= r.listen(source)
            # voice input identified
            try:
                # listen voice command in indian english 
                print("recognizing...")
                Query = r.recognize_google(audio, language='en-in')
                # display the voice command
                print("the query is printed='",Query, "'")
            except Exception as e:
                    print(e)
                    # Handling exception
                    print("please say the command again")
                    return"none"
            return Query
            #  method to input voice
            def speak(self, audio):
                # construction call for pyttsx3.init()
                engine=pyttsx3.init('sapi5')
                #  set voice type  and id
                voices= engine.getProperty('voices')
                engine.setProperty('voices[1].id')
                engine.say(audio)
                engine.runAndWait()
            # method to shutdown 
            def quitSelf(self):
                self.Speak("Should i shutdown the system")
                # input voice command
                take= self.takeCommands()
                choice = take
                if "yes" in choice:
                    # shut down
                    print("shutting down the system")
                    self.Speak("shutting down the system")
                    os.system("shutdown /s /t 1")
                    if "no" in choice:
                        # idle
                        print("thankyou sir for using me")
                        self.Speak("thankyou sir for using me")
#  Driver code 
if __name__ =='__main__':
 maam=amaancode()
 maam.quitSelf()
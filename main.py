import pyaudio
import pyttsx3
import speech_recognition as sr 
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # change number to change voces 
    # the voice inside the window 
    engine.setProperty('voice', voices[1].id)
    print("J.A.V.I.S.: " + text + "\n")
    engine.say(text)
    engine.runAndWait()

speak("Hello, what are you doing")


## add speech recognition


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...", end="")
        audio = r.listen(source)
        query = ''

        try:
            print("recognizing...", end="")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
        
        except Exception as e:
            print("Exception:" + str(e))

    
    return query.lower()

# takeCommand()


# def main():
#     said = takeCommand()
#     speak("I heard you say " + said)

# main()


def main():
    Talk = True
    while Talk == True:
        userSaid = takeCommand()
        if "hello" in userSaid:
            speak("hello")
        if "goodbye" in userSaid:
            speak("goodbye")
        if "how are you" in userSaid:
            speak("Doing well")
        if "is this video good" in userSaid:
            speak("You should like and subscribe")
        if "stop" in userSaid:
            speak("Stopping sir")
            break
        if "exit" in userSaid:
            speak("ending program")
            Talk = False
        if "open my email" in userSaid:
            speak("This is where I would run a program to open your email.")
            #Run a different function here!
        time.sleep(2)
        










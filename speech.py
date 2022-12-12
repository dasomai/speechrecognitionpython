import speech_recognition as sr 

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

takeCommand()

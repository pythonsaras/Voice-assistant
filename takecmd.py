import pyttsx3
import speech_recognition as  sr

def takecommand():
    r=sr.Recognizer()
    microphone=sr.Microphone()
    with microphone as source:
        print("Listing....")
        Speak("Listing...")
        r.pause_threshold-0.3
        audio=r.listen(source)
        try:
            print("Recognizing...")
            Speak("Recognizing...")
            Query=r.recognize_sphinx(audio)
            print(f"Your query is {Query}")
            Speak(f"Your Query is {Query}")
        except Exception as e:
            print(e)
            print("Please say that again sir..")
            Speak("Please say that again sir..")
            return "None"
        return Query
def Speak(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

# takecommand()


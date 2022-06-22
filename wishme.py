from takecmd import Speak,takecommand
import datetime

def wish():
    hour=datetime.datetime.now().hour
    if hour>0 and hour<=12:
        Speak("Good morning Sir..")
    elif hour>12 and hour<=17:
        Speak("Good afternoon Sir..")
    elif hour>17 and hour<=19:
        Speak("Good evening Sir...")
    else:
        Speak("Good night sir..")
    tim()
    today_date()
    Speak(f"I am jarvis sir. JARVIS(Just A Rather Very Intelligent System) is an artificial intelligence computer system ,Please tell me how can I help you ")
    # query=takecommand().lower()
    

def tim():
    mint=datetime.datetime.now().minute
    sec=datetime.datetime.now().second
    hour=datetime.datetime.now().hour
    Speak(f"Current time is {hour} hour {mint} minute {sec}second")
def today_date():
    to_year=datetime.datetime.now().year
    to_date=datetime.datetime.now().day
    to_month=datetime.datetime.now().month
    Speak(f"today date is {to_date} {to_month} {to_year}")


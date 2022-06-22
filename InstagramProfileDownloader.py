import instaloader
from takecmd import*
import webbrowser
import time
def profileDownload():
    bot=instaloader.Instaloader()
    Speak("Sir please enter the username correctly.")
    name=input("Enter username here : ")

    print(bot.download_profile(name,profile_pic_only=True))
    Speak("i am done sir ,profile picture save in main folder.")

def insta_profile():
    Speak("Sir please enter the username correctly.")
    name=input("Enter username here : ")
    webbrowser.open(f"www.instagram.com/{name}")
    Speak(f"Sir here is the profile of the user {name}")
    time.sleep(5)
    Speak("Sir would you like to download profile picture of this account.")
    condition=takecommand().lower()
    if "yes" in condition:
        bot=instaloader.Instaloader()
        bot.download_profile(name,profile_pic_only=True)
        Speak("i am done sir ,profile picture save in main folder. now i am ready for new command")
    else:
        pass





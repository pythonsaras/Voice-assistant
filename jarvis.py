from Image2cartoon import image2cartoon
from ScreenRecording import ScreenR
from time import time
from pdfReader import pdf_reader
from wikipediasearch import search
from wishme import wish
from takecmd import *
from SystemInfo import*
from shutdown import*
import motionDetection
from Qrgenerator import*
import Guicalander
from autoSelfieOnSmile import*
import os
import cv2
import random
import sys
import datetime


import pyautogui
def music(music_dir):
    songs=os.listdir(music_dir)
    rd=random.choice(songs)
    for song in songs:
        if song.endswith(".mp3"):
            os.startfile(os.path.join(music_dir,rd))
        elif song.endswith(".mp4"):
            os.startfile(os.path.join(music_dir,rd))

if __name__=='__main__':
    # wish()
    while True:
        query=takecommand().lower()
        timeout = 5
        try:
            from InstagramProfileDownloader import*
            from Location import location
            from news import*
            import pyjokes
            from getPhoneNumberInformation import*      
            import requests
            from requests import get
            import webbrowser
            from Sendmail import sendMail
            url=" https://www.youtube.com"
            ra = requests.get(url=url,timeout=timeout)
            print("Connected to the Internet")
            if "open instagram profile" in query:
                insta_profile()
            
            elif "ip address" in query:
                ip=get('https://api.ipify.org').text
                print(f"Your Ip address is {ip}")
                Speak(f"Your Ip address is {ip}")
            elif "wikipedia" in query:
                Speak("Searching wikipedia")
                query=query.replace("wikipedia","")
                search(query)
            elif"open youtube" in query:
                Speak("Opening youtube..")
                webbrowser.open("https://www.youtube.com")
            elif"search" in query:
                Speak("Sir ,what should I Search on google")
                cm=takecommand().lower()
                webbrowser.open(f"{cm}")
            elif"open google" in query:
                Speak("Opening google...")
                cm=takecommand().lower()
                webbrowser.open("https://www.google.com")
            elif"open stackoverflow" in query:
                Speak("Opening Stackoverflow...")
                webbrowser.open("https://www.stackoverflow.com")
            elif"open facebook" in query:
                Speak("Opening facebook...")
                webbrowser.open("https://www.facebook.com")
            elif"open w3school" in query:
                Speak("Opening w3school...")
                webbrowser.open_new_tab("https://www.w3schools.com")
            elif "send message"in query:
                import pywhatkit as kit
                kit.sendwhatmsg("+917579591044","this is demo",2,25)
            elif "play song on youtube" in query:
                Speak("Give song name Sir..")
                song=takecommand().lower()
                kit.playonyt(f"{song}")
            elif "send mail" in query:
                sendMail()
                
            elif "website ip"in query:
                import socket 
                print("Give website name for find ip address")
                Speak("Give website name for find ip address")
                host=takecommand().lower()
                try:
                    print(f"IP address of {host} is ",{socket.gethostbyname(host)})
                    Speak(f"IP address of {host} is ")
                    Speak({socket.gethostbyname(host)})        
                except Exception as e:
                    print(e)
                    Speak("Sorry sir,worng website name")
                    
            elif "joke"in query:
                joke=pyjokes.get_joke('en')
                Speak(joke)
            elif "news" in query:
                Speak("Please wait sir, Fateching the latest news")
                news()
            elif "download instagram profile"in query:
                profileDownload()

        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")
        
            if "open notepad" in query:
                path="C:\\Windows\\System32\\notepad.exe"
                os.startfile(path)
            elif "how are you" in query:
                Speak("I am fine sir what about you ")
            elif "i am also fine" in query:
                Speak("how can i help you sir")    
            elif "what are you doing"in query:
                Speak("Nothing sir i am jast try to help you")
            elif "battery" in query:
                Speak("Every thing is ok sir")

            elif "open command prompt"in query:
                os.system("Start cmd")
            elif "open camera" in query:
                cap=cv2.VideoCapture(0)
                while True:
                    _,frame=cap.read()
                    cv2.imshow("video",frame)
                    key=cv2.waitKey(1)
                    if key==ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "play music"in query:
                Speak("Playing music")
                music_dir="F:\\Music"
                music(music_dir)
            elif "play video" in query:
                Speak("Playing video")
                music_dir="F:\\video song"
                music(music_dir)

            elif "close notepad"in query:
                Speak("Ok sir ,closing notepad ")
                os.system("taskkill /f /im notepad.exe")
            elif "set alarm" in query:
                # Atime=takecommand()
                # setAtime=Atime.split(" ")
                # setAtime="%".join(setAtime)
                hr=int(datetime.datetime.now().hour)
                mnt=int(datetime.datetime.now().minute)
                # Ctime=":".join(hr,mnt)
                # Ctime=str(Ctime)
                Stime=2
                if hr==Stime:
                    # music()
                    Speak("hello")
           
            elif "system information" in query:
                cmd=takecommand().lower()
                SysInfo(cmd)
            elif"shutdown the pc" in query:
                Shutdown()
            elif"restart the pc" in query:
                restart()
            elif"sleep the pc" in query:
                sleep()
            elif "switch the window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")
            elif"generate qr" in query:
                print("Give the url to generate Qrcode")
                Speak("Give the url to generate Qrcode")
                query=takecommand().lower()
                Qrcode(query)
            elif "give number information" in query:
                print("Give your phone number with country code except + ")
                Speak("Give your phone number with country code except + ")
                query="+"+takecommand()
                PhoneInfo(query)            
            elif "open calander" in query:
                Speak("Give the year for open calander")
                year=takecommand().lower()
                Guicalander.guiCalender(year)
            elif"take selfie on smile" in query:
                AutoSelfie()
            elif "motion detect"in query:
                motionDetection.Motion()
            elif "where am i" in query:
                location()
            elif "record the screen" in query:
                Speak("Screen recording is start ")
                ScreenR()
            elif "convert image to cartoon"in query:
                Speak("Image is start converting to cartoon")
                image2cartoon()
            elif "read pdf" in query:
                Speak("reading pdf")
                pdf_reader()
            elif "play sleep song" in query:
                Speak("Playing song")
                music_dir="F:\\sleep song"
                music(music_dir)
            # Speak("Sir,do have  any other work ")
            
        # if "no thanks"or "nothing"in query:
        #     Speak("Thanks for using me sir,have a good day ")
        #     sys.exit()            
    







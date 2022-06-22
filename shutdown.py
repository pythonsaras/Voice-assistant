from takecmd import *
import os



def Shutdown():
    Speak("do you want to shutdown your pc")
    while True:
        take=takecommand()
        choice=take.lower()
        if choice=='yes':
            print("Shutting down the PC in 30 sec.")
            Speak("Shutting down  the PC in 30 sec.")
            os.system("Shutdown /s/t 30")
            break
        elif choice=='no':
            print("Thanks sir")
            Speak("thanks sir")
            break
def restart():
    Speak("do you want to restart your pc")
    
    while True:
        take=takecommand()
        choice=take.lower()
        if choice=='yes':
            print("Restarting the PC in 30 sec.")
            Speak("Restarting the PC in 30 sec.")
            os.system("Shutdown /r/t 30")
            break
        elif choice=='no':
            print("Thanks sir")
            Speak("thanks sir")
            break
def sleep():
    Speak("do you want to send Sleep mode of your pc")
    while True:
        take=takecommand()
        choice=take.lower()
        if choice=='yes':
            print("Sleeping the PC in 30 sec.")
            Speak("Sleeping the PC in 30 sec.")
            os.system("rundll32.exe powrprof.dll, SetSuspendState Sleep 30")
            break
        elif choice=='no':
            print("Thanks sir")
            Speak("thanks sir")
            break


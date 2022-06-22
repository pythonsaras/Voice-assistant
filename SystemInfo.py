from  takecmd import *
import platform
import sys

def SysInfo(query):
    
    if "system network name" in query:
        print("System network name : ",platform.node())
        Speak("System network name : ")
        Speak(platform.node())
    elif "build date" in query:
        print("Python build  date  is : ",platform.python_build)
        Speak("Python build  date  is ")
        Speak(platform.python_build)
    elif "python version" in query:
        print("Python version is : ",platform.python_version())
        Speak("Python version is ")
        Speak(platform.python_version)
    elif "operating system" in query:   
        print("Operating system is : ",platform.system)
        Speak("Operating system is")
        Speak(platform.system)
    elif"python compiler"  in query:
        print("Python compiler is : ",platform.python_compiler())
        Speak("Python compiler is")
        Speak(platform.python_compiler)
    else:         
        Speak("Worng input Sir")

import takecmd
import time
import pyautogui
def screenshot_take():
    takecmd.Speak("Sir tell me the name for this screenshot file")
    name=takecmd.takecommand().lower()
    takecmd.Speak("please sir hold the screen for few second ,i am taking screenshot")
    time.sleep(3)
    img=pyautogui.screenshot()
    img.save(f"{name}.png")
    takecmd.Speak("i am done sir ,the screenshot save in main folder. now i am ready for new command")




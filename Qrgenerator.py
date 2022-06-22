import pyqrcode
import png
from pyqrcode import QRCode
from takecmd import *

def Qrcode(query):
    url=pyqrcode.create(query)
    Name=list(query.split("."))
    query=".".join(Name[0:])
    url.png(f"F:\\python\\QRfolder\\{Name[1]}QR.png",scale=8)
    print("Sucessful")
    Speak("Sucessful")
    






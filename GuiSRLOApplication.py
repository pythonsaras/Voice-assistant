from tkinter import Button, Tk, mainloop
import os

def shutdown():
    return os.system("shutdown /s /t 5")
def restart():
    return os.system("shutdown /r /t 5")    
def logout():
    return os.system("shutdown -l")

root=Tk()
root.geometry("250x200")

root.configure(bg="green")

Button(root,text="Shutdown",command=shutdown).place(x=80,y=20)
Button(root,text="Restart",command=restart).place(x=80,y=90)
Button(root,text="Logout",command=logout).place(x=80,y=160)
root.mainloop()


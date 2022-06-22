from tkinter import*
import calendar
def guiCalender(query):
    root=Tk()
    root.title("Calender")
    year=int(query)
    myCal=calendar.calendar(year)
    calYear=Label(root,text=myCal,font="Consolas 10 bold")

    calYear.pack()
    root.mainloop()


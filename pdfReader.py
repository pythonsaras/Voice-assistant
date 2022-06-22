import PyPDF2
from takecmd import Speak
def pdf_reader():
    Speak("Give your pdf path ")
    path=input("Give your pdf path")
    book=open(path,'rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    Speak(f"Total number of pages in this book is {pages}")
    Speak("Sir please enter the page number i have to read")
    pg=int(input("Please enter the page number : "))
    page=pdfReader.getPage(pg)
    text=page.extractText()
    Speak(text)



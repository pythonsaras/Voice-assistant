from email.mime import text
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from takecmd import Speak, takecommand
def sendMail():
    Speak("what should i say?")
    query=takecommand()
    if "send a file"in query:
        email="abc@gmail.com"
        password="123"
        send_to_mail="xyz420@gmail.com"
        Speak("okey sir, what is the subject for this mail")
        query1=takecommand().lower()
        subject=query1
        Speak("and sir what is the message for this mail")
        query2=takecommand().lower()
        message=query2
        Speak("sir please enter the correct path of the file into the shell")
        file_path=input("Please enter the path here  ")
        Speak("Please wait,I am sending email now")
        msg=MIMEMultipart()
        msg['form']=email
        msg['to']=send_to_mail
        msg['subject']=subject
        msg.attach(MIMEText(message,'plain'))
        filename=os.path.basename(file_path)
        attachment=open(file_path,"rb")
        port=MIMEBase('application','octet-stream')
        port.set_payload(attachment.read())
        encoders.encode_base64(port)
        port.add_header("Content-Disposition","attachment; filename=%s"%filename)
        msg.attach(port)
        
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,send_to_mail,text)
        server.quit()
        Speak("Email has been send")


    else:
        email="abc@gmail.com"
        password="123"
        to="xyz@gmail.com"
        message=query
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,to,message)
        server.quit()
        Speak("Email has been send ")

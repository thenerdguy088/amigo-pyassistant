import socket
import requests
import time
from getpass import getpass
import pickle
import smtplib
from sys import version
import pyttsx3 as tts
from datetime import datetime
from webbrowser import open_new
from plyer import notification
from googlesearch import search
from wikipedia import summary,search
def speak(str1):
    engine=tts.init()
    engine.setProperty('rate',150)
    engine.say(str1)
    engine.runAndWait()
def trigger_notification(title1,message1):
    title=title1
    message=message1
    notification.notify(title=title1,message=message1,app_name="Amigo",timeout=15)
def is_online():
    try:
        socket.create_connection(('8.8.8.8', 53),timeout=10)
        return True
    except OSError:
        pass
    return False
def greetuser():
    hour=datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak('Good Morning')
    elif (hour >= 12) and (hour < 16):
        speak('Good Afternoon')
    elif (hour >= 16) and (hour < 21):
        speak('Good Evening')
    elif (hour >= 21):
        speak('Good night')
def translate(fl,sl,str1):
    open_new("https://translate.google.co.in/?+sl='{}'&tl='{}'&text='{}'&op=translate".format(fl,sl,str1))
    print('>>> Opening Google Translate...')
    speak('Opening Google Translate')
def search_G(str2,n):
    Y=search(str2,num_results=n)
    for A in Y:
    	open_new(A)
    speak("Opening '{}' Tabs For '{}'".format(n,str2))
    print('>>> Opening',n,'Tabs for',str2)
def search_WIKI(str3,n2):
    C=search(str3,n2)
    return C[0]
def show_WIKI(wiki_page,n3):
    print(summary(wiki_page,n3))
    speak(summary(wiki_page,n3))
def set_timer(result):
    while result>0:
        mins,secs=divmod(result, 60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        time.sleep(1)
        result -= 1
        if result==0:
            speak('Knock Knock')
            trigger_notification("Amigo - Timer Reminder",'Your time has come.')
            break
def get_external_ip():
    try:
        response=requests.get('https://api64.ipify.org?format=json')
        data=response.json()
        external_ip=data['ip']
        return external_ip
    except requests.RequestException:
        return "Could not fetch external IP."
def speak_fast(str1):
    engine=tts.init()
    engine.say(str1)
    engine.runAndWait()
def send_email(sender_email, sender_password, to_email, subject, body, smtp_server='smtp.example.com', smtp_port=587):
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            email_message = f'Subject: {subject}\n\n{body}'
            server.sendmail(sender_email, to_email, email_message)
            speak('Email sent successfully.')
            print('>>> Email sent successfully.')
    except Exception as e:
        speak(f'An error occurred: {e}')
        print(f'>>> An error occurred: {e}')

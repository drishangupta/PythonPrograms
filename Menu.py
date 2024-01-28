# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 11:58:26 2023

@author: drish
"""

import os
import pywhatkit as pwk
from datetime import datetime
import smtplib, ssl
import requests
import YouTubeMusicAPI
import tkinter
print("IM YOUR SPEECH LISTENER")
ch=input("give me a command")
ch=ch.lower()
print(ch)
a=(("run" in ch) or ("start" in ch) or ("execute" in ch) or ("turn on" in ch) or("open" in ch))
b=("notepad" in ch)
#print(bool(a)) #can be used for debugging
#print(bool(b)) #can be used for debugging
if (a and b):
    #print(bool(a))
    #print(bool(b))
    if ("dont" in ch or "do not" in ch):
        print("okay i wont run the app")
    else:
        os.system("notepad")

elif (a and ("chrome" in ch)):
    if ("dont" in ch or "do not" in ch):
        print("okay i wont run the app")
    else:
        os.system("start chrome")
        
med=("msedge" in ch) or ("microsoft edge"in ch) or ("edge" in ch) or ("browser" in ch)
if (a and med):
    if ("dont" in ch or "do not" in ch):
        print("okay i wont run the app")
    else:
        os.system("start msedge")
        
elif (a and ("facebook" in ch)):
    if ("dont" in ch or "do not" in ch):
        print("okay i wont run the app")
    else:
        os.system("start msedge www.facebook.com")
        
em=("email" in ch) or ("gmail" in ch )or ( "mail" in ch)
if (a and em ):
    if ("dont" in ch or "do not" in ch):
        print("okay i wont run the app")
    else:
        os.system("start msedge www.gmail.com")

elif (a and ("whatsapp" in ch)):
    if ("dont" in ch or "do not" in ch):
        print("okay i wont run the app")
    else:
        os.system("start msedge https://web.whatsapp.com/")
elif (a and ("youtube" in ch)):
    if ("dont" in ch or "do not" in ch):
        print("okay i wont run the app")
    else:
        os.system("start msedge www.youtube.com")
elif (a and ("reddit" in ch)):
    if ("dont" in ch or "do not" in ch):
        print("okay i wont run the app")
    else:
        os.system("start msedge www.reddit.com")
elif (a and ("linuxworld" in ch)):
    if ("dont" in ch or "do not" in ch):
        print("okay i wont run the app")
    else:
        os.system("start msedge https://www.lwindia.com/")
    
msg=(("message" in ch) or ("text" in ch) or ("ping" in ch) or ("messege" in ch))
wtp=("whatsapp" in ch) and("send" in ch or "forward" in ch)
if (msg and wtp):
    if ("dont" in ch or "do not" in ch):
        print("okay i wont run the app")
    else:
        time=datetime.now()
        timeh=int(time.strftime("%H"))
        timem=int(time.strftime("%M"))
        uptimem=timem + 2
        print("Yes i can send a text through whatsapp")
        print("")
        # using Exception Handling to avoid unexpected errors
        try: 
            messege = input("please tell me the messege you want to send")
            number= int(input("give me the number you want to send the whatsapp messge to"))
            pwk.sendwhatmsg("+91"+number, messege,timeh,uptimem)
        
            print("Message Sent!") #Prints success message in console
        
        
        # error message     
        except: 
             print("Error in sending the message")             
music=("play" in ch) or ("stream" in ch) or ("hear" in ch)
song=("music" in ch) or("song" in ch) or ("ganna" in ch)
vid=("video" in ch)or("videos" in ch)or("vedios" in ch) or("vid" in ch)
if(music and song):
    if (("dont" in ch) or ("do not" in ch)):
        print("okay i wont run the app")
    else:
        print("I will play the song")
        print("")
        songnme=input("give me the song name") 
        query: str = songnme

        result = YouTubeMusicAPI.search(query)

        if result:
            print(result["url"])
            os.system("start msedge "+ result["url"])
        else:
            print("No Result Found")
elif(music and vid):
    if (("dont" in ch) or ("do not" in ch)):
        print("okay i wont run the app")
    else:
        print("I will play the video")
        print("")
        vidnme=input("what do you want to search on youtube") 
        #print(vidnme)
        vidnme2=vidnme.replace(" ","+")
        #print(vidnme2)a
        if vidnme2: 
            print("https://www.youtube.com/results?search_query="+vidnme2)
            os.system("start msedge https://www.youtube.com/results?search_query="+vidnme2)
        else:
            print("No Result Found")
    
fm=("mail" in ch) or ("email" in ch) 
snd=("send"in ch) or ("email them" in ch) or ("forward" in ch)      
if(fm and snd):
    print("type the email address you want to be the reciever")
    print("")
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "minlinuxoth@gmail.com"  # Enter your address
    receiver_email = input("please enter the email address")  # Enter receiver address
    password = "eyhmddaiyhcxxyny"
    messegemail = input("give me the messege you want to send")
            
    messagemail=messegemail

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, messagemail)





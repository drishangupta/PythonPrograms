# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 11:56:31 2023

@author: drish
"""
import cv2
import os
import pywhatkit as pwk
from datetime import datetime
import smtplib, ssl
import requests
import YouTubeMusicAPI
import boto3
from cvzone.HandTrackingModule import HandDetector
import time
print("IM YOUR MENU GUY")
print("--------------------------------------------------------------------------------------------")
ch=input("Enter what you want me to do, I can do almost anything")
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
        uptimem=timem + 1
        print("Yes i can send a text through whatsapp")
        print("")
        # using Exception Handling to avoid unexpected errors
        try: 
                print("Please tell me the messege you want to send ")
                messege=input()
                number=input("Please tell me the number you want me to send a text to")
                pwk.sendwhatmsg("+91"+number, messege,timeh,uptimem)
        
                print("Message Sent!") #Prints success message in console
        
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
        songnme=input("Please tell me the name of the song")
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
        vidnme = input("Give me what you want to search please") 
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
    print("to prevent any errors we'll require you to type the email address by hand")
    print("")
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "minlinuxoth@gmail.com"  # Enter your address
    receiver_email = input("please enter the email address")  # Enter receiver address
    password = "eyhmddaiyhcxxyny"
    messegemail=input("Please tell me the messege you want to send ")
    messagemail=messegemail

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, messagemail)
cam=("camera" in ch) or ("photo" in ch) or ("picture" in ch) or ("pic" in ch)
openit=("open" in ch) or ("take" in ch) or ("click" in ch) or ("capture" in ch)
if(cam and openit):
    if (("dont" in ch) or ("do not" in ch)):
        print("okay i wont")
    else:
        cap=cv2.VideoCapture(1)
        stat,pic=cap.read()
        cv2.imwrite("PicTure.jpg", pic)
        cv2.imshow("mypic", pic)
        cv2.waitKey()
        cv2.destroyAllWindows()
        cap.release()
vid=("camera" in ch) or ("vid" in ch) or ("video" in ch) or ("roll" in ch)
openitt=("open" in ch) or ("take" in ch) or ("make" in ch) or ("capture" in ch)
if(vid and openitt):
    if (("dont" in ch) or ("do not" in ch)):
        print("okay i wont")
    else:
        cap=cv2.VideoCapture(1)
        while True:
            stat,pic=cap.read()
            cv2.imwrite("PicTure.mp4", pic)
            cv2.imshow("mypic", pic)
            offkey=cv2.waitKey(10)

            if offkey==13:
                break
        cv2.destroyAllWindows()    
        cap.release()
ec=("ec2" in ch) or ("aws" in ch) or ("amazon linux" in ch)or("linux" in ch)
insta=("launch" in ch) or ("make" in ch) or ("initiate" in ch ) or ("instance" in ch)
if(ec and insta):
    cap = cv2.VideoCapture(1)
    modelH = HandDetector()
    ec2 = boto3.client('ec2')
    while True:
        status , photo = cap.read()
        photo1=modelH.findHands(photo)
        photo1[1]
        cv2.imshow("hi", photo1[1])
        if cv2.waitKey(100) == 13:
            break
    
        hand = modelH.findHands(photo, draw=False)
        fingeruplist=[0,0,0,0,0]
        if hand:
            lmlist = hand[0]
            fingeruplist = modelH.fingersUp(lmlist)
            print(fingeruplist)
        if fingeruplist == [0 ,1 , 0, 0 , 0]: 
            instances = ec2.run_instances(
                   ImageId="ami-0ded8326293d3201b",
                   MinCount=1,
                   MaxCount=1,
                   InstanceType="t2.micro")  
            
            time.sleep(2)
        elif fingeruplist == [0 ,1 , 1, 0 , 0]: 
            
            instances = ec2.run_instances(
                    ImageId="ami-0ded8326293d3201b",
                    MinCount=2,
                    MaxCount=2,
                    InstanceType="t2.micro")  
             
            time.sleep(2)
        elif fingeruplist == [0 ,1 , 1, 1 , 0]: 
            
            instances = ec2.run_instances(
                    ImageId="ami-0ded8326293d3201b",
                    MinCount=3,
                    MaxCount=3,
                    InstanceType="t2.micro")  
             
            time.sleep(2)
        elif fingeruplist == [0 ,1 , 1, 1 , 1]: 
            
            instances = ec2.run_instances(
                    ImageId="ami-0ded8326293d3201b",
                    MinCount=4,
                    MaxCount=4,
                    InstanceType="t2.micro")  
             
            time.sleep(2)
        elif fingeruplist == [1 ,1 , 1, 1 , 1]: 
            
            instances = ec2.run_instances(
                    ImageId="ami-0ded8326293d3201b",
                    MinCount=5,
                    MaxCount=5,
                    InstanceType="t2.micro")  
             
            time.sleep(2)
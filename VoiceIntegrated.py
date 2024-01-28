import os
import speech_recognition as sr
import pywhatkit as pwk
from datetime import datetime
import smtplib, ssl
import requests
import YouTubeMusicAPI
print("IM YOUR SPEECH LISTENER")
r=sr.Recognizer() 
with sr.Microphone() as source1:
    r.adjust_for_ambient_noise(source1,duration=1)
    print("-----------------------------------------------------------------------------")
    print("i can listen to your commands and perform operations such as open an app which is in path variable or send whatsapp messeges etc, try me out!!")
    print("")
    print("give me a command")
    print("")
    audio2=r.listen(source1,10,10) #will listen to the microphone
    MyText = r.recognize_google(audio2) #interpret the language 
    ch=MyText.lower()
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
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2,duration=1)
                print("Please tell me the messege you want to send ")
                audiofw=r.listen(source2,10,10) #will listen to the microphone
                messege = r.recognize_google(audiofw) #interpret the language 
            with sr.Microphone() as source3:
                r.adjust_for_ambient_noise(source3,duration=1)
                print("Please tell me the number you want me to send a text to")
                audionu=r.listen(source3,10,10)
                number=r.recognize_google(audionu)
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
        with sr.Microphone() as source3:
            r.adjust_for_ambient_noise(source3,duration=1)
            print("Please tell me the name of the song")
            audiosng=r.listen(source3,15,10) #will listen to the microphone
            songnme = r.recognize_google(audiosng) #interpret the language 
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
        with sr.Microphone() as source4:
            r.adjust_for_ambient_noise(source4,duration=1)
            print("Please tell me title of the video")
            audiovid=r.listen(source4,15,10) #will listen to the microphone
            vidnme = r.recognize_google(audiovid) #interpret the language 
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
    with sr.Microphone() as source4:
                r.adjust_for_ambient_noise(source4,duration=1)
                print("Please tell me the messege you want to send ")
                audioform=r.listen(source4,10,10) #will listen to the microphone
                messegemail = r.recognize_google(audioform) #interpret the language 
            
    messagemail=messegemail

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, messagemail)





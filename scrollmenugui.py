# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 20:01:13 2023

@author: drish
"""

import tkinter as tk
from tkinter import ttk
import os
import pywhatkit as pwk
from datetime import datetime
import smtplib, ssl
import requests
#import YouTubeMusicAPI
import cv2
import boto3
from cvzone.HandTrackingModule import HandDetector
import time
import pyttsx3
import openai
key='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'
def open_notepad():
    os.system("notepad")
    # Your function code here
def open_browser():
    os.system("start msedge")

def open_facebook():
    os.system("start msedge www.facebook.com")

def open_gmail():
    os.system("start msedge www.gmail.com")

def open_whatsapp():
    os.system("start msedge https://web.whatsapp.com/")

def open_youtube():
    os.system("start msedge www.youtube.com")

def open_reddit():
    os.system("start msedge www.reddit.com")

def open_linuxworld():
    os.system("start msedge https://www.lwindia.com/")

def send_whatsapp_message():
    time = datetime.now()
    timeh = int(time.strftime("%H"))
    timem = int(time.strftime("%M"))
    uptimem = timem + 1

    number = number_entry.get()    
    message = message_entry.get()
    

    if message and number:
        pwk.sendwhatmsg_instantly("91"+number, message,wait_time=1)
    else:
        print("Please enter both the message and the number.")

    message_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

def play_song():
    song_name = song_entry.get()
    query = song_name
    

    result = YouTubeMusicAPI.search(query)

    if result:
        os.system("start msedge " + result["url"])
    else:
        print("No Result Found")

def search_video():
    video_name = video_entry.get()
    video_name = video_name.replace(" ", "+")

    if video_name:
        os.system("start msedge https://www.youtube.com/results?search_query=" + video_name)
    else:
        print("No Result Found")

def send_email():
    receiver_email = email_entry.get()
    password = "eyhmddaiyhcxxyny"
    message_email = email_message_entry.get()

    if receiver_email and message_email:
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "minlinuxoth@gmail.com"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message_email)
    else:
        print("Please enter both the receiver email and the message.")

    email_entry.delete(0, tk.END)
    email_message_entry.delete(0, tk.END)
def ec2_launch():
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
    cap.release()
def text_speech():
    text=texttosay.get()
    pyttsx3.speak(text)
def take_pic():
    cap=cv2.VideoCapture(0)
    stat,pic=cap.read()
    cv2.imwrite("PicTure.jpg", pic)
    cv2.imshow("mypic", pic)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cap.release()
def ai_talk():
    def get_ai_response(prompt):
        return openai.Completion.create(model="text-davinci-003", prompt=prompt,).choices[0].text.strip()

    def text_to_speech(text):
        pyttsx3.speak(text)

    def main():
        prompt = ai_talks_entry.get()

        if prompt:
            response = get_ai_response(prompt)
            print("AI's response:", response)
            text_to_speech(response)
    if name == "main":
        main()
        
def start_pomodoro():
    work_time = 25 * 60
    short_break_time = 5 * 60
    long_break_time = 15 * 60
    num_work_sessions = 4

    global pomodoro_active
    pomodoro_active = True

    while pomodoro_active and num_work_sessions > 0:
        countdown(work_time, "Work Time")
        if pomodoro_active:
            countdown(short_break_time, "Short Break Time")
            num_work_sessions -= 1

    if pomodoro_active:
        countdown(long_break_time, "Long Break Time")

    pomodoro_active = False
    timer_label.config(text="Pomodoro Stopped", fg="red")

def stop_pomodoro():
    global pomodoro_active
    pomodoro_active = False
    timer_label.config(text="Pomodoro Stopped", fg="red")

def countdown(seconds, session_type):
    global pomodoro_active
    while seconds and pomodoro_active:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{session_type}\n{mins:02d}:{secs:02d}", fg="black")
        root.update()
        time.sleep(1)
        seconds -= 1
    if pomodoro_active:
        timer_label.config(text="Session Complete!", fg="green")
        root.update()
        time.sleep(2)
        timer_label.config(text="")
        root.update()
def calculator():
    
    main = Tk()
    main.title('CALCULATOR')
        
    def add():
        blank.delete(0, END)
        Ans = int(num1.get()) + int(num2.get())
        blank.insert(0, Ans)
    def sub():
        blank.delete(0, END)
        Ans = int(num1.get()) - int(num2.get())
        blank.insert(0, Ans)
    def mult():
        blank.delete(0, END)
        Ans = int(num1.get()) * int(num2.get())
        blank.insert(0, Ans)
    def div():
        blank.delete(0, END)
        Ans = int(num1.get()) / int(num2.get())
        blank.insert(0, Ans)
    def clear():
        blank.delete(0, END)
        num2.delete(0, END)
        num1.delete(0, END)
    def sq():
        blank.delete(0, END)
        Ans = int(num1.get()) * int(num1.get())
        blank.insert(0, Ans)

    def sqrtt():
        blank.delete(0, END)
        h = int(num1.get())
        a = sqrt(h)
        Ans = (int(a))
        blank.insert(0, Ans)

    main.geometry('700x150')
    Label(main, text = "Enter Num 1:").grid(row=0)
    Label(main, text = "Enter Num 2:").grid(row=1)
    Label(main, text = "The Answer is:").grid(row=2)


    num1 = Entry(main)
    num2 = Entry(main)
    blank = Entry(main)


    num1.grid(row=0, column=1)
    num2.grid(row=1, column=1)
    blank.grid(row=2, column=1)


    Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W)
    Button(main, text='Add', command=add).grid(row=0, column=3, sticky=W,)
    Button(main, text='Subtract', command=sub).grid(row=0, column=4, sticky=W)
    Button(main, text='Multiply', command=mult).grid(row=0, column=5, sticky=W)
    Button(main, text='Divide', command=div).grid(row=0, column=6, sticky=W)
    Button(main, text='^2', command=sq).grid(row=0, column=7, sticky=W)
    Button(main, text='Sqrt', command=sqrtt).grid(row=0, column=8, sticky=W)
    Button(main, text='Clear', command=clear).grid(row=0, column=9, sticky=W)


def weather_fore():
    import tkinter as tk
    import speech_recognition as sr
    import pyttsx3
    import requests
    from bs4 import BeautifulSoup

    def get_weather(city_name):
        url = f"https://www.google.com/search?q=weather+in+{city_name.replace(' ', '+')}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting weather information from Google search results
        weather_info = soup.find("div", class_="BNeawe").get_text()
        return f"The weather forecast for {city_name} is {weather_info}."

    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def on_weather_button():
        city_name = city_entry.get()
        weather_text = get_weather(city_name.lower())
        weather_label.config(text=weather_text)
        speak(weather_text)

    def on_voice_command():
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        try:
            city_name = recognizer.recognize_google(audio)
            city_entry.delete(0, tk.END)
            city_entry.insert(tk.END, city_name)
            on_weather_button()
        except sr.UnknownValueError:
            print("Could not understand audio")
            speak("Sorry, I couldn't understand what you said.")
        except Exception as e:
            print(f"Error fetching results; {e}")
            speak("Sorry, there was an error fetching the weather data.")

    # Create the GUI
    root = tk.Tk()
    root.title("Weather Forecast through Voice")
    root.geometry("400x200")

    # GUI elements
    city_entry = tk.Entry(root, width=30)
    city_entry.pack(pady=20)

    weather_button = tk.Button(root, text="Get Weather", command=on_weather_button)
    weather_button.pack()

    weather_label = tk.Label(root, text="", wraplength=300, justify=tk.LEFT)
    weather_label.pack(pady=20)

    voice_button = tk.Button(root, text="Voice Input", command=on_voice_command)
    voice_button.pack()

    root.mainloop()

def img_reko():
    import boto3
    import tkinter as tk
    from tkinter import ttk

    def labels_id():
        def detect_labels(image_path):
            aws_access_key = 'AKIAYRQJZRW442CAVZTZ'
            aws_secret_key = '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'

            client = boto3.client('rekognition', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name='ap-south-1')


            with open(image_path, 'rb') as image_file:
                image_bytes = image_file.read()

            response = client.detect_labels(Image={'Bytes': image_bytes})

            return response['Labels']

        def main():
            image_path = labels_id_entry.get()
            labels = detect_labels(image_path)

            print("Labels in the image:")
            for label in labels:
                q=f"- {label['Name']} (Confidence: {label['Confidence']:.2f}%)"
                labels_id_output.insert(tk.END, q)
                print(q)


        if _name_ == "_main_":
            main()
    root = tk.Tk()
    root.title("Label For Rekognition")
    root.geometry("500x800")
    title_label = tk.Label(root, text="Labels", font=("calibri", 20, "bold"))
    title_label.pack(fill=tk.X, padx=10, pady=10)

    labels_id_entry = ttk.Entry(root)
    labels_id_entry.pack(fill=tk.X, padx=20, pady=5)

    labels_id_button = ttk.Button(root,text="Enter the file path for picture",command=labels_id)
    labels_id_button.pack(fill=tk.X, padx=20, pady=5)

    labels_id_output = tk.Text(root,height=30,width=40)
    labels_id_output.pack()

    root.mainloop()
    
def fortune():
    import random
    import tkinter as tk
    from tkinter import Label, Button

    # List of fruits
    fruits = ["May your pockets be heavy and your heart be light. May good luck pursue you each morning and night.", "Fortune favors the brave", "The best luck of all is the luck you make for yourself", "In the middle of every difficulty lies opportunity.", "The harder you work, the luckier you get"]

    def select_random_fruit():
        random_fruit = random.choice(fruits)
        result_label.config(text=f"your fortune for today is: {random_fruit.capitalize()}")

    # Create a Tkinter window
    root = tk.Tk()
    root.title("fortune for today")

    # Create a label to display the randomly selected fruit
    result_label = Label(root, text="", font=("Helvetica", 16))
    result_label.pack(padx=20, pady=20)

    # Create a button to select a random fruit
    select_button = Button(root, text="know your fortune for today", command=select_random_fruit)
    select_button.pack()

    # Start the Tkinter main loop
    root.mainloop()
    
# def local_ai():
#     from langchain.document_loaders import TextLoader
#     from langchain.embeddings import OpenAIEmbeddings
#     from langchain.text_splitter import CharacterTextSplitter
#     import os
#     file=local_ai_path_entry.get()
#     loader=TextLoader(file_path=file)
#     document=loader.load()
#     textChunk=CharacterTextSplitter(chunk_size=1000)
#     texts=textChunk.split_documents(document)
#     mykey="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"
#     myembedmodel=OpenAIEmbeddings(openai_api_key=mykey)
#     os.environ["OPENAI_API_KEY"]=mykey
#     len(texts)
#     #print(loader.load()[0].page_content)
#     from langchain.vectorstores import Pinecone as lpcone
#     import pinecone
#     pinecone.init(api_key="ab9ff52f-d87d-4f84-9b21-669a0655c2ec",
#                   environment="us-west4-gcp-free")
#     docsearch=lpcone.from_documents(documents=texts, 
#                           embedding=myembedmodel,
#                           index_name='mysummmerindex')
#     from langchain.llms import OpenAI
#     from langchain.chains import RetrievalQA
#     qs=RetrievalQA.from_chain_type(
#                 llm=OpenAI(),
#                 chain_type="stuff",
#                 retriever=docsearch.as_retriever()
#                 )
#     myquery=local_ai_query_entry.get()
#     pyttsx3.speak(qs({"query":myquery}))
#     print(qs({"query":myquery}))
# Create the main window
root = tk.Tk()
root.title("Commands Through Buttons")
root.geometry("800x800")  # Set the initial size of the window

# Create a title label
title_label = tk.Label(root, text="Commands Through Buttons", font=("calibri", 20, "bold"))
title_label.pack(fill=tk.X, padx=10, pady=10)

# Create a scrollbar
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a canvas to hold the frame with the buttons and entry fields
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=canvas.yview)

# Create a frame to hold the buttons and entry fields
main_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=main_frame, anchor=tk.NW)

# Add buttons to the main_frame
notepad_button = ttk.Button(main_frame, text="Open Notepad", command=open_notepad)
notepad_button.pack(fill=tk.X, padx=20, pady=5)

browser_button = ttk.Button(main_frame, text="Open Browser", command=open_browser)
browser_button.pack(fill=tk.X, padx=20, pady=5)

facebook_button = ttk.Button(main_frame, text="Open Facebook", command=open_facebook)
facebook_button.pack(fill=tk.X, padx=20, pady=5)

gmail_button = ttk.Button(main_frame, text="Open Gmail", command=open_gmail)
gmail_button.pack(fill=tk.X, padx=20, pady=5)

whatsapp_button = ttk.Button(main_frame, text="Open WhatsApp", command=open_whatsapp)
whatsapp_button.pack(fill=tk.X, padx=20, pady=5)

youtube_button = ttk.Button(main_frame, text="Open YouTube", command=open_youtube)
youtube_button.pack(fill=tk.X, padx=20, pady=5)

reddit_button = ttk.Button(main_frame, text="Open Reddit", command=open_reddit)
reddit_button.pack(fill=tk.X, padx=20, pady=5)

linuxworld_button = ttk.Button(main_frame, text="Open LinuxWorld", command=open_linuxworld)
linuxworld_button.pack(fill=tk.X, padx=20, pady=5)

calculator_button = ttk.Button(main_frame, text="Open Calculator", command=calculator)
calculator_button.pack(fill=tk.X, padx=20, pady=5)

weather_button = ttk.Button(main_frame, text="check weather", command=weather_fore)
weather_button.pack(fill=tk.X, padx=20, pady=5)

imagereco_button = ttk.Button(main_frame, text="Image Recognization", command=img_reko)
imagereco_button.pack(fill=tk.X, padx=20, pady=5)

yourfortune_button = ttk.Button(main_frame, text="Know Your Fortune", command=fortune)
yourfortune_button.pack(fill=tk.X, padx=20, pady=5)

# Create and position the buttons
button_pomodoro = tk.Button(root, text="Start Pomodoro", command=start_pomodoro, padx=10, pady=5, bg="#ff9800", fg="white")
button_pomodoro.pack(pady=20)

button_stop_pomodoro = tk.Button(root, text="Stop Pomodoro", command=stop_pomodoro, padx=10, pady=5, bg="#e91e63", fg="white")
button_stop_pomodoro.pack(pady=10)

timer_label = tk.Label(root, text="", font=("Helvetica", 20), bg="#f0f0f0")
timer_label.pack()



# Create entry fields and buttons for additional functionalities
message_entry = ttk.Entry(main_frame)
message_entry.pack(fill=tk.X, padx=20, pady=5)

number_entry = ttk.Entry(main_frame)
number_entry.pack(fill=tk.X, padx=20, pady=5)

send_whatsapp_button = ttk.Button(main_frame, text="Send WhatsApp Message", command=send_whatsapp_message)
send_whatsapp_button.pack(fill=tk.X, padx=20, pady=5)

song_entry = ttk.Entry(main_frame,)
song_entry.pack(fill=tk.X, padx=20, pady=5)

play_song_button = ttk.Button(main_frame, text="Play Song", command=play_song)
play_song_button.pack(fill=tk.X, padx=20, pady=5)

video_entry = ttk.Entry(main_frame,)
video_entry.pack(fill=tk.X, padx=20, pady=5)

search_video_button = ttk.Button(main_frame, text="Search Video", command=search_video)
search_video_button.pack(fill=tk.X, padx=20, pady=5)

email_entry = ttk.Entry(main_frame)
email_entry.pack(fill=tk.X, padx=20, pady=5)

email_message_entry = ttk.Entry(main_frame)
email_message_entry.pack(fill=tk.X, padx=20, pady=5)

send_email_button = ttk.Button(main_frame, text="Send Email", command=send_email)
send_email_button.pack(fill=tk.X, padx=20, pady=5)

ec2ml_button = ttk.Button(main_frame, text="Open EC2 instances Using ML", command=ec2_launch)
ec2ml_button.pack(fill=tk.X, padx=20, pady=5)

texttosay = ttk.Entry(main_frame)
texttosay.pack(fill=tk.X, padx=20, pady=5)

text_speech_button = ttk.Button(main_frame,text="Speak what you wrote",command=text_speech)
text_speech_button.pack(fill=tk.X, padx=20, pady=5)

take_pic_button = ttk.Button(main_frame,text="Take and save a picture",command=take_pic)
take_pic_button.pack(fill=tk.X, padx=20,pady=5)

ai_talks_entry = ttk.Entry(main_frame)
ai_talks_entry.pack(fill=tk.X, padx=20, pady=5)

ai_talks_button = ttk.Button(main_frame,text="Ask chat gpt",command=ai_talk)
ai_talks_button.pack(fill=tk.X, padx=20, pady=5)

# local_ai_path_entry = ttk.Entry(main_frame)
# local_ai_path_entry.pack(fill=tk.X, padx=20, pady=5)

# local_ai_query_entry = ttk.Entry(main_frame)
# local_ai_query_entry.pack(fill=tk.X, padx=20, pady=5)


# local_ai_button = ttk.Button(main_frame,text="Ask chat gpt querries from the text file u gave")
# local_ai_button.pack(fill=tk.X,padx=20,pady=5)

# ... Add more buttons similarly

# Update the scrollable region
main_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run the main event loop
root.mainloop()
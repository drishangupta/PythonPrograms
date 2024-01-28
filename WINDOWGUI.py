import os
import pywhatkit as pwk
from datetime import datetime
import smtplib, ssl
import requests
import YouTubeMusicAPI
import tkinter as tk
from tkinter import ttk
import cv2
import boto3
from cvzone.HandTrackingModule import HandDetector
import time
import pyttsx3
import openai
key='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'

def open_notepad():
    os.system("notepad")

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
        pwk.sendwhatmsg("+91" + number, message, timeh, uptimem)
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
    cap=cv2.VideoCapture(1)
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
    if __name__ == "__main__":
        main()
def local_ai():
    from langchain.document_loaders import TextLoader
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.text_splitter import CharacterTextSplitter
    import os
    file=local_ai_path_entry.get()
    loader=TextLoader(file_path=file)
    document=loader.load()
    textChunk=CharacterTextSplitter(chunk_size=1000)
    texts=textChunk.split_documents(document)
    mykey="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"
    myembedmodel=OpenAIEmbeddings(openai_api_key=mykey)
    os.environ["OPENAI_API_KEY"]=mykey
    len(texts)
    #print(loader.load()[0].page_content)
    from langchain.vectorstores import Pinecone as lpcone
    import pinecone
    pinecone.init(api_key="ab9ff52f-d87d-4f84-9b21-669a0655c2ec",
                  environment="us-west4-gcp-free")
    docsearch=lpcone.from_documents(documents=texts, 
                          embedding=myembedmodel,
                          index_name='mysummmerindex')
    from langchain.llms import OpenAI
    from langchain.chains import RetrievalQA
    qs=RetrievalQA.from_chain_type(
                llm=OpenAI(),
                chain_type="stuff",
                retriever=docsearch.as_retriever()
                )
    myquery=local_ai_query_entry.get()
    print(qs({"query":myquery}))
# Create the main window
root = tk.Tk()
root.title("Commands Through Buttons")
root.geometry("800x800")  # Set the initial size of the window

# Create a title label
title_label = tk.Label(root, text="Commands Through Buttons", font=("calibri", 20, "bold"), bg="#dfe6e9", fg="#2d3436")
title_label.pack(fill=tk.X, padx=10, pady=10)

main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas = tk.Canvas(main_frame, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=canvas.yview)

frame_window = canvas.create_window((0, 0), window=main_frame, anchor=tk.NW)


# Create buttons for each specific command and functionality
style = ttk.Style()
style.configure('TButton', font=('calibri', 12, 'bold'), foreground='#2d3436', background='#dfe6e9')

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

local_ai_path_entry = ttk.Entry(main_frame)
local_ai_path_entry.pack(fill=tk.X, padx=20, pady=5)

local_ai_query_entry = ttk.Entry(main_frame)
local_ai_query_entry.pack(fill=tk.X, padx=20, pady=5)


local_ai_button = ttk.Button(main_frame,text="Ask chat gpt querries from the text file u gave")
local_ai_button.pack(fill=tk.X,padx=20,pady=5)

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

main_frame.bind("<Configure>", on_frame_configure)
# Run the main event loop
root.mainloop()

import os
import pywhatkit as pwk
from datetime import datetime
import smtplib, ssl
import requests
import YouTubeMusicAPI
import tkinter as tk

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
    uptimem = timem + 2

    message = message_entry.get()
    number = number_entry.get()

    pwk.sendwhatmsg("+91" + number, message, timeh, uptimem)
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

    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "minlinuxoth@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message_email)
    email_entry.delete(0, tk.END)
    email_message_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Speech Listener")

# Create buttons for each specific command and functionality
notepad_button = tk.Button(root, text="Open Notepad", command=open_notepad)
notepad_button.pack()

browser_button = tk.Button(root, text="Open Browser", command=open_browser)
browser_button.pack()

facebook_button = tk.Button(root, text="Open Facebook", command=open_facebook)
facebook_button.pack()

gmail_button = tk.Button(root, text="Open Gmail", command=open_gmail)
gmail_button.pack()

whatsapp_button = tk.Button(root, text="Open WhatsApp", command=open_whatsapp)
whatsapp_button.pack()

youtube_button = tk.Button(root, text="Open YouTube", command=open_youtube)
youtube_button.pack()

reddit_button = tk.Button(root, text="Open Reddit", command=open_reddit)
reddit_button.pack()

linuxworld_button = tk.Button(root, text="Open LinuxWorld", command=open_linuxworld)
linuxworld_button.pack()

# Create entry fields and buttons for additional functionalities
message_entry = tk.Entry(root)
message_entry.pack()

number_entry = tk.Entry(root)
number_entry.pack()

send_whatsapp_button = tk.Button(root, text="Send WhatsApp Message", command=send_whatsapp_message)
send_whatsapp_button.pack()

song_entry = tk.Entry(root)
song_entry.pack()

play_song_button = tk.Button(root, text="Play Song", command=play_song)
play_song_button.pack()

video_entry = tk.Entry(root)
video_entry.pack()

search_video_button = tk.Button(root, text="Search Video", command=search_video)
search_video_button.pack()

email_entry = tk.Entry(root)
email_entry.pack()

email_message_entry = tk.Entry(root)
email_message_entry.pack()

send_email_button = tk.Button(root, text="Send Email", command=send_email)
send_email_button.pack()

# Run the main event loop
root.mainloop()

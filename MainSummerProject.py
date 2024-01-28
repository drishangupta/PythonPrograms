import tkinter as tk
from tkinter import ttk
import os
import pywhatkit as pwk
from datetime import datetime
import smtplib, ssl
import requests
import cv2
import boto3
import random
from cvzone.HandTrackingModule import HandDetector
import time
import pyttsx3
import openai
from tkinter import *
from math import *
import tkinter
from tkinter.messagebox import *
from tkinter.filedialog import *
import speech_recognition as sr
import YouTubeMusicAPI

    
key='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'
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
    number = number_entry.get()    
    message = message_entry.get()
    

    if message and number:
        pwk.sendwhatmsg_instantly("+91" + number, message)
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
    cap = cv2.VideoCapture(0)
    modelH = HandDetector()
    ec2 = boto3.client('ec2')
    while True:
        status , photo = cap.read()
        photo1=modelH.findHands(photo)
        photo1[1]
        cv2.imshow("hi", photo1[1])
        if cv2.waitKey(100) == 13:
            break
    
        hand = modelH.findHands(photo, draw=True)
        fingeruplist=[0,0,0,0,0]
        if hand:
            print(hand)
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
    if __name__ == "__main__":
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


        if __name__ == "__main__":
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

def paint():
    class PaintApp:
        def __init__(self, root):
            self.root = root
            self.canvas_width = 800
            self.canvas_height = 600
            self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white", bd=3, relief=tk.SUNKEN)
            self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.setup_navbar()
            self.setup_tools()
            self.setup_events()
            self.prev_x = None
            self.prev_y = None

        def setup_navbar(self):
            self.navbar = tk.Menu(self.root)
            self.root.config(menu=self.navbar)

            # File menu
            self.file_menu = tk.Menu(self.navbar, tearoff=False)
            self.navbar.add_cascade(label="File", menu=self.file_menu)
            self.file_menu.add_command(label="Save Snapshot", command=self.take_snapshot)
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Exit", command=self.root.quit)

            # Edit menu
            self.edit_menu = tk.Menu(self.navbar, tearoff=False)
            self.navbar.add_cascade(label="Edit", menu=self.edit_menu)
            self.edit_menu.add_command(label="Undo", command=self.undo)

        def setup_tools(self):
            self.selected_tool = "pen"
            self.colors = ["black", "red", "green", "blue", "yellow", "orange", "purple"]
            self.selected_color = self.colors[0]
            self.brush_sizes = [2, 4, 6, 8]
            self.selected_size = self.brush_sizes[0]
            self.pen_types = ["line", "round", "square", "arrow", "diamond"]
            self.selected_pen_type = self.pen_types[0]

            self.tool_frame = ttk.LabelFrame(self.root, text="Tools")
            self.tool_frame.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.Y)

            self.pen_button = ttk.Button(self.tool_frame, text="Pen", command=self.select_pen_tool)
            self.pen_button.pack(side=tk.TOP, padx=5, pady=5)



            self.brush_size_label = ttk.Label(self.tool_frame, text="Brush Size:")
            self.brush_size_label.pack(side=tk.TOP, padx=5, pady=5)

            self.brush_size_combobox = ttk.Combobox(self.tool_frame, values=self.brush_sizes, state="readonly")
            self.brush_size_combobox.current(0)
            self.brush_size_combobox.pack(side=tk.TOP, padx=5, pady=5)
            self.brush_size_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_size(int(self.brush_size_combobox.get())))

            self.color_label = ttk.Label(self.tool_frame, text="Color:")
            self.color_label.pack(side=tk.TOP, padx=5, pady=5)

            self.color_combobox = ttk.Combobox(self.tool_frame, values=self.colors, state="readonly")
            self.color_combobox.current(0)
            self.color_combobox.pack(side=tk.TOP, padx=5, pady=5)
            self.color_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_color(self.color_combobox.get()))

            self.pen_type_label = ttk.Label(self.tool_frame, text="Pen Type:")
            self.pen_type_label.pack(side=tk.TOP, padx=5, pady=5)

            self.pen_type_combobox = ttk.Combobox(self.tool_frame, values=self.pen_types, state="readonly")
            self.pen_type_combobox.current(0)
            self.pen_type_combobox.pack(side=tk.TOP, padx=5, pady=5)
            self.pen_type_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_pen_type(self.pen_type_combobox.get()))

            self.clear_button = ttk.Button(self.tool_frame, text="Clear Canvas", command=self.clear_canvas)
            self.clear_button.pack(side=tk.TOP, padx=5, pady=5)

        def setup_events(self):
            self.canvas.bind("<B1-Motion>", self.draw)
            self.canvas.bind("<ButtonRelease-1>", self.release)

        def select_pen_tool(self):
            self.selected_tool = "pen"



        def select_size(self, size):
            self.selected_size = size

        def select_color(self, color):
            self.selected_color = color

        def select_pen_type(self, pen_type):
            self.selected_pen_type = pen_type

        def draw(self, event):
            if self.selected_tool == "pen":
                if self.prev_x is not None and self.prev_y is not None:
                    if self.selected_pen_type == "line":
                        self.canvas.create_line(self.prev_x, self.prev_y, event.x, event.y, fill=self.selected_color,
                                                width=self.selected_size, smooth=True)
                    elif self.selected_pen_type == "round":
                        x1 = event.x - self.selected_size
                        y1 = event.y - self.selected_size
                        x2 = event.x + self.selected_size
                        y2 = event.y + self.selected_size
                        self.canvas.create_oval(x1, y1, x2, y2, fill=self.selected_color, outline=self.selected_color)
                    elif self.selected_pen_type == "square":
                        x1 = event.x - self.selected_size
                        y1 = event.y - self.selected_size
                        x2 = event.x + self.selected_size
                        y2 = event.y + self.selected_size
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.selected_color, outline=self.selected_color)
                    elif self.selected_pen_type == "arrow":
                        x1 = event.x - self.selected_size
                        y1 = event.y - self.selected_size
                        x2 = event.x + self.selected_size
                        y2 = event.y + self.selected_size
                        self.canvas.create_polygon(x1, y1, x1, y2, event.x, y2, fill=self.selected_color,
                                                   outline=self.selected_color)
                    elif self.selected_pen_type == "diamond":
                        x1 = event.x - self.selected_size
                        y1 = event.y
                        x2 = event.x
                        y2 = event.y - self.selected_size
                        x3 = event.x + self.selected_size
                        y3 = event.y
                        x4 = event.x
                        y4 = event.y + self.selected_size
                        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=self.selected_color,
                                                   outline=self.selected_color)
                self.prev_x = event.x
                self.prev_y = event.y

        def release(self, event):
            self.prev_x = None
            self.prev_y = None

        def clear_canvas(self):
            self.canvas.delete("all")

        def take_snapshot(self):
            self.canvas.postscript(file="snapshot.eps")

        def undo(self):
            items = self.canvas.find_all()
            if items:
                self.canvas.delete(items[-1])

    if __name__ == "__main__":
        root = tk.Tk()
        root.title("Paint Application")
        app = PaintApp(root)
        root.mainloop()
def team_17():
    os.system("start msedge 13.233.92.181")

    
def translate():
    import boto3

    def translate_text(text, source_language_code, target_language_code):
        session = boto3.Session(
            aws_access_key_id='AKIA2TXNNOJIOU42BJHD',
            aws_secret_access_key='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',
            region_name='ap-south-1'
        )

        translate = session.client('translate')

        response = translate.translate_text(
            Text=text,
            SourceLanguageCode=source_language_code,
            TargetLanguageCode=target_language_code
        )
    
        translated_text = response['TranslatedText']
        return translated_text

    def translate_button_click():
        source_text = source_text_entry.get()
        source_language = source_language_combo.get()
        target_language = target_language_combo.get()

        translated_text = translate_text(source_text, source_language, target_language)
        translated_text_label.config(text=f"Translated text: {translated_text}")

    # Create the main window
    root = tk.Tk()
    root.title("Text Translator")

    # Create GUI elements
    source_text_label = tk.Label(root, text="Enter source text:")
    source_text_entry = tk.Entry(root)

    source_language_label = tk.Label(root, text="Select source language:")
    source_language_combo = ttk.Combobox(root, values=["en", "fr", "es","ru","sr","sv","ur","ta","te"])  

    target_language_label = tk.Label(root, text="Select target language:")
    target_language_combo = ttk.Combobox(root, values=["fr", "en", "es","ru","sr","sv","ur","ta","te"])  

    translate_button = tk.Button(root, text="Translate", command=translate_button_click)
    translated_text_label = tk.Label(root, text="Translated text: ")

    # Arrange GUI elements using grid layout
    source_text_label.grid(row=0, column=0, padx=10, pady=10)
    source_text_entry.grid(row=0, column=1, padx=10, pady=10)
    source_language_label.grid(row=1, column=0, padx=10, pady=10)
    source_language_combo.grid(row=1, column=1, padx=10, pady=10)
    target_language_label.grid(row=2, column=0, padx=10, pady=10)
    target_language_combo.grid(row=2, column=1, padx=10, pady=10)
    translate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    translated_text_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()

def notepad():


    class Notepad:

        __root = Tk()

        # default window width and height
        __thisWidth = 300
        __thisHeight = 300
        _thisTextArea = Text(_root)
        _thisMenuBar = Menu(_root)
        _thisFileMenu = Menu(_thisMenuBar, tearoff=0)
        _thisEditMenu = Menu(_thisMenuBar, tearoff=0)
        _thisHelpMenu = Menu(_thisMenuBar, tearoff=0)

        # To add scrollbar
        _thisScrollBar = Scrollbar(_thisTextArea)	
        __file = None

        def __init__(self,**kwargs):

            # Set icon
            try:
                    self.__root.wm_iconbitmap("Notepad.ico")
            except:
                    pass

            # Set window size (the default is 300x300)

            try:
                self.__thisWidth = kwargs['width']
            except KeyError:
                pass

            try:
                self.__thisHeight = kwargs['height']
            except KeyError:
                pass

            # Set the window text
            self.__root.title("Untitled - Notepad")

            # Center the window
            screenWidth = self.__root.winfo_screenwidth()
            screenHeight = self.__root.winfo_screenheight()

            # For left-align
            left = (screenWidth / 2) - (self.__thisWidth / 2)

            # For right-align
            top = (screenHeight / 2) - (self.__thisHeight /2)

            # For top and bottom
            self._root.geometry('%dx%d+%d+%d' % (self._thisWidth,
                                                self.__thisHeight,
                                                left, top))

            # To make the textarea auto resizable
            self.__root.grid_rowconfigure(0, weight=1)
            self.__root.grid_columnconfigure(0, weight=1)

            # Add controls (widget)
            self.__thisTextArea.grid(sticky = N + E + S + W)

            # To open new file
            self.__thisFileMenu.add_command(label="New",
                                      command=self.__newFile)

            # To open a already existing file
            self.__thisFileMenu.add_command(label="Open",
                                            command=self.__openFile)

            # To save current file
            self.__thisFileMenu.add_command(label="Save",
                                            command=self.__saveFile)

            # To create a line in the dialog
            self.__thisFileMenu.add_separator()
            self.__thisFileMenu.add_command(label="Exit",
                                            command=self.__quitApplication)
            self.__thisMenuBar.add_cascade(label="File",
                                        menu=self.__thisFileMenu)

            # To give a feature of cut
            self.__thisEditMenu.add_command(label="Cut",
                                            command=self.__cut)

            # to give a feature of copy
            self.__thisEditMenu.add_command(label="Copy",
                                            command=self.__copy)

            # To give a feature of paste
            self.__thisEditMenu.add_command(label="Paste",
                                            command=self.__paste)

            # To give a feature of editing
            self.__thisMenuBar.add_cascade(label="Edit",
                                        menu=self.__thisEditMenu)

            # To create a feature of description of the notepad
            self.__thisHelpMenu.add_command(label="About Notepad",
                                            command=self.__showAbout)
            self.__thisMenuBar.add_cascade(label="Help",
                                        menu=self.__thisHelpMenu)

            self._root.config(menu=self._thisMenuBar)

            self.__thisScrollBar.pack(side=RIGHT,fill=Y)

            # Scrollbar will adjust automatically according to the content	
            self._thisScrollBar.config(command=self._thisTextArea.yview)	
            self._thisTextArea.config(yscrollcommand=self._thisScrollBar.set)


        def __quitApplication(self):
            self.__root.destroy()
            # exit()

        def __showAbout(self):
            showinfo("Notepad","Mrinal Verma")

        def __openFile(self):

            self.__file = askopenfilename(defaultextension=".txt",
                                        filetypes=[("All Files","."),
                                            ("Text Documents","*.txt")])

            if self.__file == "":

                # no file to open
                self.__file = None
            else:

                # Try to open the file
                # set the window title
                self._root.title(os.path.basename(self._file) + " - Notepad")
                self.__thisTextArea.delete(1.0,END)

                file = open(self.__file,"r")

                self.__thisTextArea.insert(1.0,file.read())

                file.close()


        def __newFile(self):
            self.__root.title("Untitled - Notepad")
            self.__file = None
            self.__thisTextArea.delete(1.0,END)

        def __saveFile(self):

            if self.__file == None:
                # Save as new file
                self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                                defaultextension=".txt",
                                                filetypes=[("All Files","."),
                                                    ("Text Documents","*.txt")])

                if self.__file == "":
                    self.__file = None
                else:

                    # Try to save the file
                    file = open(self.__file,"w")
                    file.write(self.__thisTextArea.get(1.0,END))
                    file.close()

                    # Change the window title
                    self._root.title(os.path.basename(self._file) + " - Notepad")


            else:
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()

        def __cut(self):
            self.__thisTextArea.event_generate("<<Cut>>")

        def __copy(self):
            self.__thisTextArea.event_generate("<<Copy>>")

        def __paste(self):
            self.__thisTextArea.event_generate("<<Paste>>")

        def run(self):

            # Run main application
            self.__root.mainloop()




    # Run main application
    notepad = Notepad(width=600,height=400)
    notepad.run()
    
def cropvideo():
    cap=cv2.VideoCapture(1)
    while True:

        status,photo=cap.read()
        a=photo[200:450,300:500]
        photo[0:250,0:200]=a
        cv2.imshow("myphoto" ,photo)
        if cv2.waitKey(1)==13:
            break       
    cv2.destroyAllWindows()
    cap.release()

def voicecommand():
    def voice():
        r = sr.Recognizer()
        with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1, duration=0.5)
            output_label.config(text="Give me a command")
            output_label.update()
            audio2 = r.listen(source1, timeout=10, phrase_time_limit=10)  # Will listen to the microphone

            try:
                MyText = r.recognize_google(audio2)  # Interpret the language
                ch = MyText.lower()
                output_label.config(text=ch)
                os.system(ch)
            except sr.UnknownValueError:
                output_label.config(text="Could not understand audio")
            except sr.RequestError:
                output_label.config(text="Could not request results")

    # Create the main window
    root = tk.Tk()
    root.title("Voice Command App")

    # Create GUI elements
    start_button = tk.Button(root, text="Start Listening", command=voice)
    start_button.pack(pady=20)

    output_label = tk.Label(root, text="", font=("Helvetica", 12))
    output_label.pack()

    # Start the Tkinter event loop
    root.mainloop()

    
def game():
    class GuessNumberGame:
        def __init__(self, root):
            self.root = root
            self.root.title("Guess the Number Game")

            self.target_number = random.randint(1, 100)
            self.attempts = 0

            self.label = tk.Label(root, text="Guess a number between 1 and 100:")
            self.label.pack(pady=10)

            self.entry = tk.Entry(root)
            self.entry.pack(pady=5)

            self.result_label = tk.Label(root, text="")
            self.result_label.pack(pady=5)

            self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
            self.submit_button.pack(pady=10)

            self.new_game_button = tk.Button(root, text="New Game", command=self.new_game)
            self.new_game_button.pack()

        def check_guess(self):
            self.attempts += 1
            user_guess = int(self.entry.get())

            if user_guess < self.target_number:
                self.result_label.config(text="Higher!")
            elif user_guess > self.target_number:
                self.result_label.config(text="Lower!")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.")
                self.submit_button.config(state=tk.DISABLED)

        def new_game(self):
            self.target_number = random.randint(1, 100)
            self.attempts = 0
            self.result_label.config(text="")
            self.entry.delete(0, tk.END)
            self.submit_button.config(state=tk.NORMAL)

    if __name__ == "__main__":
        root = tk.Tk()
        game = GuessNumberGame(root)
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

team_17_button = ttk.Button(main_frame, text="The Team 17", command=team_17, )
team_17_button.pack(fill=tk.X,padx=155,pady=5)

# Add buttons to the main_frame

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

openpaint_button = ttk.Button(main_frame, text="Open Paint", command=paint)
openpaint_button.pack(fill=tk.X, padx=20, pady=5)

translate_button = ttk.Button(main_frame, text="translate", command=translate)
translate_button.pack(fill=tk.X, padx=20, pady=5)

videocrop_button = ttk.Button(main_frame, text="Live Video Crop", command=cropvideo)
videocrop_button.pack(fill=tk.X, padx=20, pady=5)

voiceassistance_button = ttk.Button(main_frame, text="Command through speech", command=voicecommand)
voiceassistance_button.pack(fill=tk.X, padx=20, pady=5)

gessnumber_button = ttk.Button(main_frame, text="Guess the number GAME", command=game)
gessnumber_button.pack(fill=tk.X, padx=20, pady=5)

#yournotepad_button = ttk.Button(main_frame, text="Open notepad", command=notepad)
#yournotepad_button.pack(fill=tk.X, padx=20, pady=5)

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

video_entry = ttk.Entry(main_frame,)
video_entry.pack(fill=tk.X, padx=20, pady=5)

search_video_button = ttk.Button(main_frame, text="Search Video", command=search_video)
search_video_button.pack(fill=tk.X, padx=20, pady=5)

song_entry = ttk.Entry(main_frame,)
song_entry.pack(fill=tk.X, padx=20, pady=5)

play_song_button = ttk.Button(main_frame, text="Play Song", command=play_song)
play_song_button.pack(fill=tk.X, padx=20, pady=5)

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
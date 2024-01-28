# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:07:09 2023

@author: drish
"""

import tkinter as tk
import pyttsx3
import openai

# Set your OpenAI API key
openai.api_key = "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"

class AITalkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Talk")

        self.prompt_label = tk.Label(root, text="Enter your prompt:")
        self.prompt_label.pack()

        self.ai_talks_entry = tk.Entry(root)
        self.ai_talks_entry.pack()

        self.response_label = tk.Label(root, text="AI's response:")
        self.response_label.pack()

        self.response_text = tk.Text(root, height=10, width=40)
        self.response_text.pack()

        self.talk_button = tk.Button(root, text="Talk to AI", command=self.main)
        self.talk_button.pack()

    def get_ai_response(self, prompt):
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt).choices[0].text.strip()
        return response

    def text_to_speech(self, text):
        pyttsx3.speak(text)

    def main(self):
        prompt = self.ai_talks_entry.get()

        if prompt:
            response = self.get_ai_response(prompt)
            self.response_text.delete(1.0, tk.END)  # Clear previous text
            self.response_text.insert(tk.END, response)
            self.text_to_speech(response)

if __name__ == "__main__":
    root = tk.Tk()
    app = AITalkApp(root)
    root.mainloop()

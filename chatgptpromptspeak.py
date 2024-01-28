# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:03:48 2023

@author: drish
"""

import openai
import pyttsx3
key='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'

# Set your OpenAI API key
openai.api_key = key

def get_ai_response(prompt):
    return openai.Completion.create(model="text-davinci-003", prompt=prompt,).choices[0].text.strip()

def text_to_speech(text):
    pyttsx3.speak(text)

def main():
    prompt = input("Enter your prompt: ")

    if prompt:
        response = get_ai_response(prompt)
        print("AI's response:", response)
        text_to_speech(response)

if __name__ == "__main__":
    main() 30.22222...2......2.0.2
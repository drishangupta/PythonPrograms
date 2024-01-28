# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:55:04 2023

@author: drish
"""

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
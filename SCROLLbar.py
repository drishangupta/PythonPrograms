# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 16:45:36 2023

@author: drish
"""

import tkinter as tk
from tkinter import ttk
import os

def open_notepad():
    os.system("notepad")


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

# ... Add more buttons similarly

# Update the scrollable region
main_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run the main event loop
root.mainloop()

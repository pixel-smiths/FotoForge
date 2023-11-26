import tkinter as tk
from tkinter import colorchooser

def open_color_selector():
    color = colorchooser.askcolor()[1]
    button.config(bg=color)

root = tk.Tk()

button = tk.Button(root, text="Select Color", command=open_color_selector)
button.pack()

root.mainloop()

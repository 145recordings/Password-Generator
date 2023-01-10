import tkinter as tk
from gui import Gui

#version 1.0.0
#created by Franklin
#1-10-2023

root = tk.Tk()
gui = Gui(root)
root.resizable(False,False)
root.geometry("500x200")
root.title("Password Generator v1.0.0")
root.mainloop()
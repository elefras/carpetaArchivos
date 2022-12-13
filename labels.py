import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

root=tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

image=Image.open("logo.png").resize((64, 64))
photo=ImageTk.PhotoImage(image)
label.ttk.Label(root, image=photo, padding=5)
label.pack()

label=ttk.Label(root, text="Hellow World", padding=20)
label.config(font=("Arial", 20))
label.pack()


root.mainloop()

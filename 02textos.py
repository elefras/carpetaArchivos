from tkinter import *

ventana=Tk()
ventana.geometry("500x500")

texto=Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="black",
    padx=500,
    pady=20,
    font=("Consolas", 30)
    )
texto.pack()

texto=Label(ventana, text="Bienvenido a mi programa")
texto.config(
    height=2,
    bg="orange",
    font=("Arial", 18),
    cursor="circle"
    )
texto.pack(anchor=W)

texto=Label(ventana, text="Bienvenido a mi programa")
texto.config(
    height=2,
    bg="red",
    font=("Arial", 18),
    cursor="circle"
    )
texto.pack(anchor=NW)

ventana.mainloop()

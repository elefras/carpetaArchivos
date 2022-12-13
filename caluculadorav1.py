import tkinter as tk
from tkinter import ttk

def uno():
    num="1"
    entry.insert(tk.END, num)
    print("1")

def dos():
    num="2"
    entry.insert(tk.END, num)
    print("2")

def tres(): 
    num="3"
    entry.insert(tk.END, num)
    print("3")

def cuatro():
    num="4"
    entry.insert(tk.END, num)
    print("4")

def cinco():
    num="5"
    entry.insert(tk.END, num)
    print("5")

def seis():
    num="6"
    entry.insert(tk.END, num)
    print("6")

def siete():
    num="7"
    entry.insert(tk.END, num)
    print("7")

def ocho():
    num="8"
    entry.insert(tk.END, num)
    print("8")

def nueve():
    num="9"
    entry.insert(tk.END, num)
    print("9")

def cero():
    num="0"
    entry.insert(tk.END, num)
    print("0")

#OPERACIONES

def sumaN():
    global a
    a=int(entry.get())
    entry.delete(0, "end")
    print(a)
    return

def res():
    b=int(entry.get())
    suma=a+b
    print(suma)

root=tk.Tk()
#root.geometry("300x300")
root.resizable(False, False)
root.title("Calculadora")

label=ttk.Label(root, text="Resultados")
label.grid(row=0, column=0)

entry=ttk.Entry(root, width=10)
entry.grid(row=0, column=1)


#Primera columna

uno=ttk.Button(text="1", command=uno)
uno.grid(row=1, column=0)

dos=ttk.Button(text="2", command=dos)
dos.grid(row=1, column=1)

tres=ttk.Button(text="3", command=tres)
tres.grid(row=1, column=2)

suma=ttk.Button(text="+", command=sumaN)
suma.grid(row=1, column=3)

#Segunda columna

cuatro=ttk.Button(text="4", command=cuatro)
cuatro.grid(row=2, column=0)

cinco=ttk.Button(text="5", command=cinco)
cinco.grid(row=2, column=1)

seis=ttk.Button(text="6", command=seis)
seis.grid(row=2, column=2)

#Tercera columna

siete=ttk.Button(text="7", command=siete)
siete.grid(row=3, column=0)

ocho=ttk.Button(text="8", command=ocho)
ocho.grid(row=3, column=1)

nueve=ttk.Button(text="9", command=nueve)
nueve.grid(row=3, column=2)

#Cuarta columna

cero=ttk.Button(text="0", command=cero)
cero.grid(row=4, column=1)

resultado=ttk.Button(text="=", command=res)
resultado.grid(row=4, column=3)



root.mainloop()

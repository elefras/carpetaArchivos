import tkinter as tk
from tkinter import *
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
x=False
y=False
z=False
w=False

def sumaN():
    global a, x
    a=float(entry.get())
    entry.delete(0, "end")
    print(a)
    x=True
    return 

def restaN():
    global a, y
    a=float(entry.get())
    entry.delete(0, "end")
    print(a)
    y=True
    return

def multN():
    global a, z
    a=float(entry.get())
    entry.delete(0, "end")
    print(a)
    z=True
    return

def divN():
    global a, w
    a=float(entry.get())
    entry.delete(0, "end")
    print(a)
    w=True
    return

def res():
    global x, y, z, w
    
    if x:
        b=int(entry.get())
        suma=float(a+b)
        print(suma)
        entry.delete(0, "end")
        entry.insert(tk.END, suma)
        
    elif y:
        b=int(entry.get())
        resta=float(a-b)
        print(resta)
        entry.delete(0, "end")
        entry.insert(tk.END, resta)
        
    elif z:
        b=int(entry.get())
        mult=float(a*b)
        print(mult)
        entry.delete(0, "end")
        entry.insert(tk.END, mult)

    elif w:
        b=int(entry.get())
        div=a/b
        print(div)
        entry.delete(0, "end")
        entry.insert(tk.END, div)

    x=False
    y=False
    z=False
    w=False
    
def borrar():
    entry.delete(0, "end")
        
root=tk.Tk()
#root.geometry("300x300")
root.resizable(False, False)
root.title("Calculadora")
#root.configure(bg='red')

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

resta=ttk.Button(text="-", command=restaN)
resta.grid(row=2, column=3)


#Tercera columna

siete=ttk.Button(text="7", command=siete)
siete.grid(row=3, column=0)

ocho=ttk.Button(text="8", command=ocho)
ocho.grid(row=3, column=1)

nueve=ttk.Button(text="9", command=nueve)
nueve.grid(row=3, column=2)

mult=ttk.Button(text="x", command=multN)
mult.grid(row=3, column=3)


#Cuarta columna

ac=ttk.Button(text="AC", command=borrar)
ac.grid(row=4, column=0)

cero=ttk.Button(text="0", command=cero)
cero.grid(row=4, column=1)

resultado=ttk.Button(root, text="=", command=res)
resultado.grid(row=4, column=2)

division=ttk.Button(text="/", command=divN)
division.grid(row=4, column=3)



root.mainloop()

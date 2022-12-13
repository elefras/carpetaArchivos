import xlsxwriter as xls
from io import open
import pathlib
import shutil
import os
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
#root.geometry("300x300")
root.resizable(False, False)
root.title("Excel pruebas")

def crear():
    if not os.path.isfile('./miLibro.xlsx'):
        libro=xls.Workbook('miLibro.xlsx')
        libro.close()
        print("Libro creado")
    else:
        print("El libro ya ha sido creado")

def escribir():
    hoja=libro.add_worksheet()
    hoja.write('B2', 'Hola mundo')
    hoja.write(4,4,"Prueba")
    libro.close()
    print("Texto agregado")

crearB=ttk.Button(text="Crear", command=crear)
crearB.grid(row=0, column=0)
escribirB=ttk.Button(text="Escribir", command=escribir)
escribirB.grid(row=0, column=1)



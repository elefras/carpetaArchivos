from io import open
import pathlib
import shutil
import os

"""
#abrir archivo
ruta=str(pathlib.Path().absolute())+"/fichero_texto.txt"
archivo=open(ruta, "a+")

#escribir
archivo.write("Soy un texto metido desde python\n")


#cerrar archivo
archivo.close()


#abrir archivo
ruta=str(pathlib.Path().absolute())+"/fichero_texto.txt"
archivo_lectura=open(ruta, "r")

#leer contenido

contenido=archivo_lectura.read()
print(contenido)

#leer contenido y guardarlo en lista
lista=archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    lista_frase=frase.split()
    print(lista_frase)
"""

#copiar archivo
"""
ruta_original=str(pathlib.Path().absolute())+"/fichero_texto.txt"
ruta_nueva=str(pathlib.Path().absolute())+"/fichero_texto_N.txt"
shutil.copyfile(ruta_original, ruta_nueva)
"""

#mover archivo
"""
ruta_original=str(pathlib.Path().absolute())+"/fichero_texto_N.txt"
ruta_nueva=str(pathlib.Path().absolute())+"/fichero_texto_nueva.txt"
shutil.move(ruta_original, ruta_nueva)
"""

#eliminar
"""
ruta_nueva=str(pathlib.Path().absolute())+"/fichero_texto_nueva.txt"
os.remove(ruta_nueva)
"""

#comprobar si existe
import os.path
#print(os.path.abspath("./"))
"""
if os.path.isfile(os.path.abspath("./")+"/fichero_texto.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")
"""

#DIRECTORIOS
#Crear carpeta
import os
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
    print("Carpeta creada")
else:
    print("Ya existe el direcotrio")

#eliminar
#os.rmdir("./mi_carpeta")

#Copiar una carpeta
"""
ruta_original="./mi_carpeta"
ruta_nueva="./mi_carpeta_copiada"

shutil.copytree(ruta_original, ruta_nueva)
"""

print("contenido de mi carpeta")
contenido=os.listdir("./mi_carpeta")
#print(contenido)
for fichero in contenido:
    print("Fichero: "+fichero)

















    









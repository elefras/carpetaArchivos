"""
Ejercicio 2: Hacer un programa que pida la anchura y la altura de
un rectangulo y que lo dibuje con un *
"""

def dibujar(ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ",end="")
        print()

ancho=int(input("Digite el ancho: "))
alto=int(input("Digite el alto: "))

dibujar(ancho, alto)

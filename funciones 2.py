#Ejemplo 1
"""
def muestraNombres():
    print("Victor")
    print("Ely")
    print("Efra")

muestraNombres()
"""
#Ejemplo 2
"""
def mostrartunombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad>=18:
        print("Y eres mayor de edad")
    else:
        print("Error")

mostrartunombre("Efra", 19)
mostrartunombre("Efra", 18)
nombre=input("Introduce tu name: ")
edad=int(input("Introduce tu name: "))
mostrartunombre(nombre, edad)
"""

#Ejemplo 3
"""
def tabla(numero):
    print(f"Tabla del multiplicar del numero: {numero}")
    for contador in range(11):
        operacion=numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

tabla(2)
"""

#Ejemplo 3.1
"""
for numero_tabla in range(1,11):
    tabla(numero_tabla)
"""

#Ejemplo 4
"""
def getEmpleado(nombre, dni=False):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if dni!=False:
        print(f"DNI: {dni}")

getEmpleado("Efra")
"""

#Ejemplo 5
"""
#Ejemplo return
def saludame(nombre):
    saludo=f"Hola, saludos {nombre}"
    return saludo
print(saludame("Efra"))
"""

#Ejemplo 6
"""
def calculadora(numero1, numero2, basicas=False):
    suma=numero1+numero2
    resta=numero1-numero2
    multi=numero1*numero2
    division=numero1/numero2

    cadena=""

    if basicas!=False:
        cadena+="Suma: "+str(suma)
        cadena+="\n"
        cadena+="Resta: "+str(resta)
        cadena+="\n"
    else:
        cadena+="Multiplicacion: "+str(multi)
        cadena+="\n"
        cadena+="Division: "+str(division)

    return cadena

print(calculadora(5,5, True))
"""

#Ejemplo 7
"""
def getNombre(nombre):
    texto=f"El nombre es: {nombre}"
    return texto

def getApellido(apellido):
    texto=f"El apellido es: {apellido}"
    return apellido

def devuelvetodo(nombre, apellido):
    texto=getNombre(nombre)+"\n"+getApellido(apellido)
    return texto

print(devuelvetodo("Efra", "DLT"))
print(getNombre("Ely"), getApellido("Corona"))
"""

#Ejemplo 8

dimeelyear=lambda year:f"El ano es {year*50}"
print(dimeelyear(1998))
















    

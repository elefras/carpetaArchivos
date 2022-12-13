nombre="Efrain"

#funciones generales
print(nombre)
print(type(nombre))

#detectar el tipado
comprobar=isinstance(nombre, str)
if comprobar:
    print("Es una string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

frase="     mi contenidoooo   "
print(frase)
print(frase.strip())

year=2022
print(year)
del year
print(year)
 

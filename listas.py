#Listas

pelicula="Batman"

#definir lista
peliculas=["Batman", "Spiderman", "El senor de los anillos"]
cantantes=list(('2Pac', 'Drake', 'Jenni'))
years=list(range(2020,2050))
variada=["Victor", 30, 4, 4, True, "Texto"]
"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""
#Indices
"""
print(peliculas[1])
print(peliculas[-1])
print(cantantes[1:3])
print(peliculas[1:])

peliculas[1]="EFRAS"
print(peliculas)
"""


#anadir elementos a una lista
"""
cantantes.append("Zoe")
print(cantantes)
"""

"""
nueva_peli=""
while nueva_peli!="Parar":
    nueva_peli=input("Introduce la nueva pelicula: ")

    if nueva_peli!="Parar":
        peliculas.append(nueva_peli)

#recorrer lista
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
"""

"""
contactos=[
    [
        'Antonio',
        'antonio@ibm.com'
    ],
    [
        'Efrain',
        'efrain@ibm.com'
    ],
    [
        'Shava',
        'shavador@ibm.com'
    ]
]

#print(contactos[1][0])
for contacto in contactos:
    #print(f"{contactos.index(contacto)+1}. {contacto}")
    print(contacto)

"""

#Ejemplo
"""
cantantes=['Zoe', 'Led Zeppelin', 'Pink Floyd']
numeros=[1,2,8,7,5]

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

#Eliminar elementos
cantantes.append("El nacho")
cantantes.insert(3, "ROCK")
print(cantantes)

#eliminar
cantantes.pop(0)
cantantes.remove('El nacho')
print(cantantes)

#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print('ROCK' in cantantes)

#Contar elementos
print(cantantes)
print(len(cantantes))

#Cuantas veces aparece un numero
print(numeros.count(8))

#Conseguir indice
print(cantantes.index("Pink Floyd"))

#Unir listas
cantantes.extend(numeros)
print(cantantes)
"""





























    






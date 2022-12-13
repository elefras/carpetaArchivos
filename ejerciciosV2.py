#Ejercicios 1
"""
numeros=[10,32,53,84,22,45,76,67]
print(numeros)
numeros.sort()
print(numeros)
print(len(numeros))

for i in numeros:
    print(f"Elemento: {i}")

ele=""
while ele!=True:
    elemento=int(input("Digite el elemento a buscar: "))
    ele=elemento in numeros
    print(ele)

if ele:
    print(f"La posicion en la tabla es {numeros.index(elemento)+1}")
"""

#Ejercicio 2
"""
num=0
lista=[]

while num<120:
    num=int(input("Digite un numero: "))
    lista.append(num)

for i in lista:
    print(f"Elementos: {i}")
"""



#Ejercicio 1

pais="Mexico"
continente="America"

print(pais)
print(continente)

print(type(pais))
print(type(continente))


#Ejercicios 2
"""
par=0

for par in range(0,102,2):
    print(par)

for contador in range(1, 121):
    if contador%2==0:
        print(f"{contador} es par")
    else:
        print(f"{contador} es impar")

"""
#Ejercicio 3
"""
for num in range(1,61):
    print(f"El cuadrado del numero {num} es {num*num}")
"""

#Ejercicio 4
"""
num1=int(input("Digite el primer numero: "))
num2=int(input("Digite el segundo numero: "))

for num in range(num1+1, num2):
    print(num)
"""

#Ejercicio 5
"""
for num in range(1,11):
    print(f"##########Tabla del {num} ############")
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
"""

#Ejercicio 6
"""
num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))

for contador in range(num1, num2):
    if contador%2==0:
        num=0
    else:
        print(contador)
"""

#Ejercicio 7
"""
num1=float(input("Digite el numero: "))
porcentaje=float(input("Digite el porcentaje: "))
mult=num1*porcentaje
res=mult/100
print(f"El porciento ({porcentaje}%) de {num1} es {res}")
"""

#Ejercicio 8
"""
num=0
while num!=111:
    num=int(input("Digite un numero: "))
    print(num)
"""

#Ejercicio 9
"""
aprobado=0
reprobado=0

for num in range(1,6):
    calf=int(input("Digite la calificacion: "))
    if calf>6 and calf<=10:
        aprobado+=1
    elif calf>0 and calf<=6:
        reprobado+=1
    else:
        print("Cantidad incorrecta, 1<>10")

print(f"Las personas que aprobaron fueron: {aprobado}")
print(f"Las personas que reprobaron fueron: {reprobado}")
"""









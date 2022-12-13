def agregarcliente(cliente, nombre, apellido, dni):
    cliente={}
    cliente['nombre']=nombre
    cliente['apellido']=apellido
    cliente['dni']=dni
    clientes.append(cliente)

def mostrarclientes(clientes):
    for i in clientes:
        print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, DNI: {i['dni']}")

def mostrarcliente(clientes, dni):
    for i in clientes:
        if i['dni']==dni:
            print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, DNI: {i['dni']}")
            return True
    return False

def eliminarcliente(clientes, dni):
    for i in clientes:
        if i['dni']==dni:
            clientes.remove(i)
            return True
    return False

clientes=[]#Lista

while True:
    print(""".:Menu:.
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por DNI
4. Eliminar cliente
5. Salir""")
    opcion=int(input("Digite una opcion: "))
    print()

    if opcion==1:
        nombre=input("Nombre del clinte: ")
        apellido=input("Apellido del cliente: ")
        dni=input("DNI del clinte: ")
        agregarcliente(clientes,nombre,apellido,dni)

    elif opcion==2:
        mostrarclientes(clientes)

    elif opcion==3:
        dni=input("DNI del cliente: ")
        if mostrarcliente(clientes, dni):
            print("Cliente encontrado")
        else:
            print("Cliente no encontrado")

    elif opcion==4:
        dni=input("Digite el dni: ")
        if eliminarcliente(clientes,dni):
            print("Cliente eliminado")
        else:
            print("Cliente no encontrado")

    elif opcion==5:
        break

    else:
        print("Error, eliga otra opcion")
        
                
        

    

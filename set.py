#SET
"""
personas={
    "Victor",
    "Enlly",
    "Efra"
    }

personas.add("Paco")
personas.remove("Efra")

print(type(personas))
print(personas)
"""

#Diccionario
"""
persona={
    "nombre": "Victor",
    "apellidos": "Robles",
    "web": "efra.com"
    }

print(type(persona))
print(persona["web"])
"""

#Lista con diccionario
contactos=[
    {
        'nombre': 'Antonio',
        'email': 'efra.ibm.com'
        },
    {
        'nombre': 'Jesus',
        'email': 'jesus.ibm.com'
        },
    {
        'nombre': 'Reyes',
        'email': 'reyes.ibm.com'
        }
    ]

contactos[0]['nombre']="Efra"
print(contactos[0]['nombre'])

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")











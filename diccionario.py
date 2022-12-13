#Diccionario

tabla=[
    {
        'categoria':'Accion',
        'juegos':["GTA", "Call of Duty", "PUGB"]
    },
    {
        'categoria':'Aventura',
        'juegos':["Assins", "Crash", "Prince"]
    },
    {
        'categoria':'Deportes',
        'juegos':["Fifa", "PRO 21", "Moto GP"]
    }
]

for categoria in tabla:
    print(f"-------{categoria['categoria']}-------")
    for juegos in categoria['juegos']:
        print(juegos)
        
    

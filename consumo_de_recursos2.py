import random
dificultad = input("Elige dificultad (facil, media, dificil): ")

# recursos y consumos según dificultad
if dificultad == "facil":
    comida = 100
    agua = 100
    energia = 100
    personas = 10
    salud = 100
    dano = 10   # daño cuando falta recurso
    probabilidad_evento = 0.7  # probabilidad de eventos aleatorios
    if random.random() < probabilidad_evento:
        evento = random.choice(["Small Supply Loss","Minor Generator Glitch","Short Water Leak",
                                "Mild Illness","Equipment Damage","Cold Night"])
        print("Evento del dia:", evento)
        
    
elif dificultad == "media":
    comida = 60
    agua = 60
    energia = 60
    personas = 5
    salud = 60
    dano = 5    # menos daño
    probabilidad_evento = 0.5  # probabilidad de eventos aleatorios

elif dificultad == "dificil":
    comida = 35
    agua = 35
    energia = 35
    personas = 2
    salud = 50
    dano = 3    # aún menos daño
    probabilidad_evento = 0.4  # probabilidad de eventos aleatorios

comida_consumida = 1
consumo_agua = 1
consumo_energia = 1

dia = 1
while salud > 0:

    print("\nDía", dia)

    total_comida_consumida = personas * comida_consumida
    total_agua_consumida = personas * consumo_agua
    total_energia_consumida = personas * consumo_energia    

    # VERIFICAR COMIDA
    if comida < total_comida_consumida:
        salud -= dano
        print("No hay suficiente comida. Salud disminuida a", salud)
    else:
        comida -= total_comida_consumida
        print("Comida restante:", comida)

    # VERIFICAR AGUA
    if agua < total_agua_consumida:
        salud -= dano
        print("No hay suficiente agua. Salud disminuida a", salud)
    else:
        agua -= total_agua_consumida
        print("Agua restante:", agua)

    # ENERGÍA SIEMPRE SE CONSUME SI HAY
    if energia >= total_energia_consumida:
        energia -= total_energia_consumida
        print("Energía restante:", energia)

    print("Salud actual:", salud)

    dia += 1

print("\nLa colonia ha colapsado")
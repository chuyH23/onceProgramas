import random


def eleccion_computadora():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)


def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif (
        (jugador == "piedra" and computadora == "tijeras") or
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "tijeras" and computadora == "papel")
    ):
        return "Ganaste"
    else:
        return "Computadora gana"


def jugar_piedra_papel_tijeras():
    print("Bienvenido a Piedra, Papel o Tijeras!")
    while True:
        jugador = input("Elige piedra, papel o tijeras (o 'salir' para terminar el juego): ").lower()
        if jugador == "salir":
            break
        if jugador not in ["piedra", "papel", "tijeras"]:
            print("Entrada no válida. Por favor, elige piedra, papel o tijeras.")
            continue

        computadora = eleccion_computadora()
        print(f"La computadora eligió: {computadora}")

        resultado = determinar_ganador(jugador, computadora)
        print(f"Resultado: {resultado}\n")


jugar_piedra_papel_tijeras()
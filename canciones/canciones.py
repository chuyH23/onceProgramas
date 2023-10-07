canciones = [
     "nataelCano",
    "GunsRoses",
]

print("elije una de las siguientes 2 canciones:\n")
for i, cancion in enumerate(canciones, start=1):
    print(f"{i}. {cancion}")


while True:
    try:
        seleccion = int(input("\nelije un numero entre el 1-2: "))
        if 1 <= seleccion <= 2:
            break
        else:
            print("Número no válido. Por favor, ingresa un número del 1 al 2.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número del 1 al 2.")

letra_cancion = ""
if seleccion == 1:
    letra_cancion = """
    ------- nataelCano ------------
    ajuaaa mi ranchgo y pal norte, era una ladyyy gaga tutsi y lavanda amonossssss.
    """

elif seleccion == 2:
    letra_cancion = """
    ------- GunsRoses ------------
    se toca un solo de guitarra bien epico y luego se canta como se debe.
    """

print(f"\nelejiste: {canciones[seleccion - 1]} aqui viene:\n")
print(letra_cancion)


opcion = input("Presiona '*' para elegir otra canción o cualquier otra tecla para salir: ")
if opcion != '*':
    print("¡Hasta luego!")
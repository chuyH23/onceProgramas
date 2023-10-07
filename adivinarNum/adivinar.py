import random


numero_secreto = random.randint(1, 50)


intentos = 0

while True:
    intento = input("Adivina el número entre 1 y 50 (o escribe 'salir' para salir): ")

    
    if intento.lower() == 'salir':
        print(f"El número secreto era {numero_secreto}. que pues ya te rendiste mi chavo")
        break

    try:
        intento = int(intento)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    intentos += 1

    if intento < numero_secreto:
        print("El número secreto es mayor. Intenta nuevamente.")
    elif intento > numero_secreto:
        print("El número secreto es menor. Intenta nuevamente.")
    else:
        print(f"Felicidades, ¡adivinaste el número secreto {numero_secreto} en {intentos} intentos!")
        break
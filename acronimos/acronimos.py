
def convertir_a_sigla(frase):
   
    palabras = frase.split()

   
    sigla = ""

    for palabra in palabras:
        sigla += palabra[0].upper()  

    return sigla

entrada = input("Ingrese una frase para convertirla en sigla: ")

sigla = convertir_a_sigla(entrada)
print(f"Acronimo: {sigla}")
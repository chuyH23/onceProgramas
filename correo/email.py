
correo_electronico = input("Por favor, ingresa tu dirección de correo electrónico: ")


usuario, dominio = correo_electronico.split("@")


dominios_populares = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]


if dominio in dominios_populares:
    print(f"¡Hola {usuario.capitalize()}! Veo que tu correo electrónico está registrado con un proveedor popular como {dominio}. ¡Eso es genial!")
else:
    print(f"¡Hola {usuario.capitalize()}! Veo que tienes un correo electrónico personalizado con el dominio {dominio}.")
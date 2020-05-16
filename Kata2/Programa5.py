# Vamos a aprender qué es un While

password = "1234"
intentosMax = 5
intento = 1

passwordIntroducida = input("\nIntroduzca su contraseña: ")

while password != passwordIntroducida and intento < intentosMax:
    passwordIntroducida = input("\nContraseña erronea, prueba de nuevo (quedan " + str(intentosMax - intento) + " intentos): ")
    intento = intento + 1


if  intento == intentosMax:
    print("\nHas superado los intentos permitidos.\n")
else:
    print("\nContraseña correcta.\n")

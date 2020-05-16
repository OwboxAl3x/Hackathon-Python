# Vamos a aprender qué es un While

password = "1234"
INTENTOS_MAX = 5
intento = 1

passwordIntroducida = input("\nIntroduzca su contraseña: ")

while password != passwordIntroducida and intento < INTENTOS_MAX:
    passwordIntroducida = input("\nContraseña erronea, prueba de nuevo (quedan " + str(INTENTOS_MAX - intento) + " intentos): ")
    intento = intento + 1


if  intento == INTENTOS_MAX:
    print("\nHas superado los intentos permitidos.\n")
else:
    print("\nContraseña correcta.\n")

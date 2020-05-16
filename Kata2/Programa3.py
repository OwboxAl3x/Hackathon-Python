#Vamos a crear un programa de compra de entradas

edad = input("\nIntroduzca su edad, por favor: ")

edad = int(edad)

if edad < 4:
    print("\nLa entrada es gratis.\n")
elif edad >= 4 and edad <= 18:
    print("\nEl precio de la entrada es de 5€.\n")
else:
    print("\nEl precio de la entrada es de 10€.\n")    


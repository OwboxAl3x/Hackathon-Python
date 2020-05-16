# Vamos a crear un inventario de una juguetería

juguetes = ("Oso de peluche", "Barbie", "Coche", "Nenuco")

print("\nInventario:\n")

for i in range(len(juguetes)):
    print(str(i+1) + ". " + juguetes[i])
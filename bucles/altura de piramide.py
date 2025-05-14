# ingrese el numero de bloques para determinar la altura de la piramida
#recuerde que por cada capa, siempre la de abajo sera una mas que la de arriba
bloques = int(input("Ingrese el numero de bloques: "))
altura = 0
capas = 1
while bloques >= capas:
    altura = altura +1
    bloques = bloques - capas

    capas = capas+1

print("La altura de la piramide es: ", altura)
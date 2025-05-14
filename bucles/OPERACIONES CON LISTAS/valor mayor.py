lista = [17,3,11,5,1,9,7,33,13]

mayor = lista[0]

for i in range (1, len(lista)):# 1 significa que el ciclo comienza desde pos. 1
    if lista[i] > mayor: #compara el segundo numero de la lista que es 3 con la variable mayor que es 17 en este caso
        mayor = lista[i]# si el numero de la lista es mayor que la variable mayor se iguala la variable

print(mayor)
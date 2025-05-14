list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)


# solucion

list_1 = [1]
list_2 = list_1[:] #Una rebanada de este tipo crea una nueva lista (de destino), tomando elementos de la lista de origen - los elementos de los índices desde elcomenzarhasta el finalaleta - 1.
list_1[0] = 2
print(list_2)


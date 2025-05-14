my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False # variable booleana para verificar si se encontro el numero

for i in range(len(my_list)):
    found = my_list[i] == to_find # compara el numero found con la posicion de la lista
    if found: # si es igual rompe el ciclo
        break

if found:
    print("Elemento encontrado en el índice", i) # si encuentra el numero, imprime que en efecto
else:
    print("ausente") #caso contrario dira que el numero no se encontro en la lista


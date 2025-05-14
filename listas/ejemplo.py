numeros = [1,2,3,4,5]
print("numeros son: ", numeros)

numeros[0] = 19
print("numeros son: ",numeros)

numeros [4] = numeros[0]
print("lista actualizada: ", numeros)

# eliminar numeros de lista

del numeros[1]
print("cantidad de numeros en la lista: ")
print(len(numeros))
print(numeros)
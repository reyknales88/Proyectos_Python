numeros = [1,2,3,4,5]
print("lista de numeros:",numeros)

n1 = int (input("reemplace el número del medio en la lista con un número entero ingresado por el usuario "))
numeros[2] = n1
print("lista actualizada: ", numeros)


del numeros[4]
print("cantidad de posiciones en el arreglo: ",len(numeros))
print(numeros)
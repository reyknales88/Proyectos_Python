impar = 0
par = 0


numero = int(input("ingrese un numero par o impar: "))
while  numero != 0:

    if numero %2 == 1:
        impar = impar + 1

    else:
        par = par + 1

    numero = int(input("ingrese un numero o ingrese 0 para salir"))



print("numeros pares: ",par, " numeros impares: ",impar)




numTop = -999999

numero = int(input("ingrese un numero: "))

while numero != -1:
    if numero > numTop:
        numTop = numero

    numero = int(input("ingrese un numero: o escribe -1 para salir"))
                 
                 
                 

print("el numero mas grande es: ", numTop)


year = int(input("Introduce el año: "))

if year <1582:
    print("No dentro del periodo de la era gregoriana!!!")

else :
    if year % 4 != 0:
        print("Año Comun")
    elif year % 100 != 0:
        print("Año Bisiesto")

    elif year % 400 != 0:
        print("año Comun")
    else :
        print("Año bisiesto")

        #Si la condición es if es FALSO, el programa verifica las condiciones de los bloques Elif posteriores: el primer Elif que sea Verdadero es el que se ejecuta. 
        # Si todas las condiciones son FALSO, se ejecutará el bloque else.
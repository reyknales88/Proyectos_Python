palabra = input("ingrese una palabra: ")

#pasar palabra a mayuscula

palabra = palabra.upper

# ciclo para devorar palabras con continue

for letra in palabra:
    if letra in ['A','E','I','O','U']:
        continue
    print(letra)


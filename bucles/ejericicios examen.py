x = 1

while x < 11:
    if x %2 != 0:
        print(x)
        x += 1


#Crea un programa con unparabucle y unromperDeclaración. El programa debe iterar sobre los caracteres de una dirección de correo electrónico y salir del bucle cuando llega al@símbolo e imprimir la parte antes@En una sola línea. Utilice el siguiente esquema:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break # Line of code.
        print(ch, end="")# Line of code.
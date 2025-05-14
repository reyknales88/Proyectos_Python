#En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (que aún permanece sin demostrar) que puede describirse de la siguiente manera:

# Tome cualquier número entero no negativo y distinto de cero y nómbreloc0;
# Si es parejo, evalúa uno nuevoc0comoc0 ÷ 2;
# De lo contrario, si es extraño, evalúa uno nuevo.c0como3 × c0 + 1;
# sic0 ≠ 1, volver al punto 2.
# La hipótesis dice que independientemente del valor inicial dec0, siempre irá a 1.

# Por supuesto, es una tarea extremadamente compleja utilizar un ordenador para demostrar 
# la hipótesis de cualquier número natural (puede que incluso se necesite inteligencia artificial),
#  pero puedes utilizar Python para comprobar algunos números individuales. Quizá incluso encuentres el que
#  refute la hipótesis.

# Escriba un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sigue
#  siendo diferente de 1. También queremos que cuentes los pasos necesarios para alcanzar el objetivo.
#  Tu código debería mostrar todos los valores intermedios dec0, también.

numero = int (input("Ingrese un numero a evaluar: "))
contador = 0;
while numero != 1:
    if numero % 2 == 0:
        contador += 1
        numero = numero /2
        print(numero )
    else:
        contador = contador +1
        numero = 3 * numero +1
        print(numero)

print("ha salido del bucle porque su numero dio igual a 1 ")
print("por lo tanto la cantidad de pasos para llegar a 1 fueron de: ", contador) 

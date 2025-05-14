num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
num3 = int(input("Ingrese tercer numero: "))

max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3

print("el numero mayor es: ", max)
num1 = int(input("Ingrese numero uno: "))
num2 = int(input("Ingrese numero dos: "))

if num1 > num2:
    print(" el numero ",num1, "es mayor que ", num2)

else:
    print("el numero ", num2, "es mayor que ", num1)



# OTRA FORMA DE HACERLO
# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
elif number1<number2:
    larger_number = number2
    print("El número más grande es:",larger_number)
if number1 == number2:
    print("los numeros son iguales!!")

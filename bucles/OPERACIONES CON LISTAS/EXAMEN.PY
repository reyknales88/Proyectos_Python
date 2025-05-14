lista_1 = ["A","B","C"]
list_2 = lista_1
list_3 = list_2

del lista_1[0]
del list_2[0]

print(list_3)

# EJERCICIO 2

lista_1 = ["A","B","C"]
list_2 = lista_1
list_3 = list_2

del lista_1[0]
del list_2

print(list_3)


#EJERCICIO 3

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0] # elimina A
del list_2[:] # elimina todo

print(list_3)


#EJERCICIO 4

list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

# cada lista es una copia independiente ya que se creo una nueva

# EJERCICIO 5
my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # output True
print("A" not in my_list)  # output True
print(3 not in my_list)  # output True
print(False in my_list)  # output False


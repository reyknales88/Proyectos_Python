#crear lista
los_beatles = []

#agregar miembros e imprimir
los_beatles.append("John_lenon")
los_beatles.append("paul")
los_beatles.append("Harrison")
print(los_beatles)

for i in range(2):
    los_beatles.append(input("ingrese nuevo miembro:  "))


print(los_beatles)

#borrar elementos de una lista

del los_beatles[4]
del los_beatles[3]

print(los_beatles)

#insertar un nombre

los_beatles.insert(3,"ringo")
print(los_beatles)

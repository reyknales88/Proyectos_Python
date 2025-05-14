lista = [2,5,8,1,5,3,7,5,2]
rep = lista[0]
print(lista)
rep = 0
nueva_lista = []
for i in lista:
    if i not in nueva_lista:
        nueva_lista.append(i)
    else:
        rep += 1    
        
    

print("la nueva lista sin numeros repetidos son: ",nueva_lista)
print("cantidad de numeros eliminados: ",rep)
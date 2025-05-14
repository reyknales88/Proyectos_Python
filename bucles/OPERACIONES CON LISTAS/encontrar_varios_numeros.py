ticket = [19,24,10,5,13,28]
sorteados = [19,8,24,10,67,89]

acertados = 0

for numbers in sorteados:
    if numbers in ticket:
        acertados = acertados +1
        
print("cantidad de aciertos: ",acertados)
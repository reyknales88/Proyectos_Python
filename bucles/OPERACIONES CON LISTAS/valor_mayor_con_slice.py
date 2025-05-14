my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]: # my_list[1:] es un slicing que crea una sublista que excluye el primer elemento. En este caso, la sublista 
    if i > largest:
        largest = i

print(largest)


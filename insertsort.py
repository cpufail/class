def insertionsort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

print("ordenados")
lista = [2, 3, 4, 5, 6, 7, 8, 9]
insertionsort(lista)
print(lista)
print("ordenados inverso")
lista = [9, 8, 7, 6, 5, 4, 3, 2]
insertionsort(lista)
print(lista)
print("duplicados")
lista = [2, 2, 2, 3, 4, 5, 5, 6]
insertionsort(lista)
print(lista)

print("aleatorios")
lista = [4, 3, 1, 9, 5]
insertionsort(lista)
print(lista)
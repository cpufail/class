lista = [2,6,1,8,9]

for i in range(len(lista)):
    for j in range(0,(len(lista)-1)-i):
        if (lista[j]>lista[j+1]):
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]= aux

print(lista)


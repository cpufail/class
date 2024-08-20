def bubblesort(lista):
    for i in range(len(lista)):
        for j in range(0,(len(lista)-1)-i):
            if (lista[j]>lista[j+1]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]= aux

lista = [2,7,1,5,9]
bubblesort(lista)
print(lista)
lista = [6,5,4,3,2]
bubblesort(lista)
print(lista)

lista=[1,2,3,4]
bubblesort(lista)
print(lista)

lista=[3,2,2,2,2,3,3]
bubblesort(lista)
print(lista)



import time
from bubblesort import bubblesort
from insertsort import insertionsort
from mergeshort import mergesort
from selectionsort import selection_sort
from shellsort import shell_sort
from quicksort import quicksort
lista = [2,5,71,2,3]
lista2 = [1,2,3,4,5]
lista3 = [1,3,3,2,2,2,3,3]
lista4 = [6,5,4,3,2,1]

inicio = time.time()
bubblesort(lista)
bubblesort(lista2)
bubblesort(lista3)
bubblesort(lista4)
print("bubble aleatorio",lista)
print("bubble sequencia",lista2)
print("bubble repetido",lista3)
print("bubble inverso",lista4)
fim = time.time()
print(fim-inicio)

inicio = time.time()
insertionsort(lista)
insertionsort(lista2)
insertionsort(lista3)
insertionsort(lista4)
print("insertsort aleatorio",lista)
print("insertsort sequencia",lista2)
print("insertsort repetido",lista3)
print("insertsort inverso",lista4)
fim = time.time()
print(fim-inicio)

inicio = time.time()
selection_sort(lista)
selection_sort(lista2)
selection_sort(lista3)
selection_sort(lista4)
print("selection aleatorio",lista)
print("selection sequencia",lista2)
print("selection repetido",lista3)
print("selection inverso",lista4)
fim = time.time()
print(fim-inicio)

inicio = time.time()
shell_sort(lista)
shell_sort(lista2)
shell_sort(lista3)
shell_sort(lista4)
print("shellsort aleatorio",lista)
print("shellsort sequencia",lista2)
print("shellsort repetido",lista3)
print("shellsort inverso",lista4)
fim = time.time()
print(fim-inicio)

inicio = time.time()
mergesort(lista, 0, len(lista) - 1)
mergesort(lista2, 0, len(lista2) - 1)
mergesort(lista3, 0, len(lista3) - 1)
mergesort(lista4, 0, len(lista4) - 1)
print("merge aleatorio",lista)
print("merge sequencia",lista2)
print("merge repetido",lista3)
print("merge inverso",lista4)
fim = time.time()
print(fim-inicio)


inicio = time.time()
quicksort(lista, 0, len(lista) - 1)
quicksort(lista2, 0, len(lista2) - 1)
quicksort(lista3, 0, len(lista3) - 1)
quicksort(lista4, 0, len(lista4) - 1)
print("quicksort:", lista)
print("quicksort:", lista2)
print("quicksort:", lista3)
print("quicksort:", lista4)
fim = time.time()
print(fim-inicio)

def heapmax(l, n, i):
    maior = i 
    esquerda = 2 * i + 1  
    direita = 2 * i + 2  

    if esquerda < n and l[esquerda] > l[maior]:
        maior = esquerda

    if direita < n and l[direita] > l[maior]:
        maior = direita

    if maior != i:
        l[i], l[maior] = l[maior], l[i]

        heapmax(l, n, maior)

def heapsort(l):
    n = len(l)

    for i in range(n // 2 - 1, -1, -1):
        heapmax(l, n, i)

    for i in range(n - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        heapmax(l, i, 0)

l = [2,5,9,1,20,5]
heapsort(l)
print("lay ordenado é:", l)



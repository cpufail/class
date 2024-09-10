def heapify(arr, n, i):
    menor = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] < arr[menor]:
        menor = esquerda
    if direita < n and arr[direita] < arr[menor]:
        menor = direita
    if menor != i:
        arr[i], arr[menor] = arr[menor], arr[i]

        heapify(arr, n, menor)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
arr = [8,2,19,2,6,8,4]
heapsort(arr)
print("Array ordenado é:", arr)

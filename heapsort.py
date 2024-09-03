def heapsort(arr, n, i):
    maior = i
    l = 2 * i + 1 
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        maior = l
    if r < n and arr[maior] < arr[r]:
        maior = r
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapsort(arr, n, maior)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapsort(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapsort(arr, i, 0)

arr = [2, 5, 3, 8, 6, 5, 4, 7]
heapSort(arr)
print("Array ordenado é:", arr)

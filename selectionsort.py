def selection_sort(data):
    n = len(data)
    for i in range(n-1):
        menor_id = i 
        for j in range(i + 1, n):
            if data[j] < data[menor_id]:
                menor_id = j 
        data[i], data[menor_id] = data[menor_id], data[i]

def test_selection_sort():
    data = [64, 25, 12, 22, 11]
    print("Lista original:", data)
    
    selection_sort(data)
    print("Lista ordenada:", data)

test_selection_sort()

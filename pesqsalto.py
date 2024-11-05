import math

def pesq_salto(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1  

def test_pesq_salto():
    # Vetor de exemplo ordenado
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Casos de teste
    test_cases = [
        (5, 5),   # Elemento está presente
        (0, 0),   # Primeiro elemento
        (10, 10), # Último elemento
        (11, -1), # Elemento não presente
        (-1, -1), # Elemento negativo não presente
        (3, 3),   # Elemento no meio
    ]
    
    for x, expected in test_cases:
        result = pesq_salto(arr, x)
        assert result == expected, f"Teste falhou para {x}: esperado {expected}, obtido {result}"
    
    print("Todos os testes passaram!")

# Executar os testes
test_pesq_salto()



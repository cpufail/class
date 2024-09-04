def troca(v, a, b):
    tmp = v[a]
    v[a] = v[b]
    v[b] = tmp

def particiona(V, inicio, final):
    esq = inicio
    dir = final
    pivo = V[inicio]

    while esq < dir:
        while esq <= final and V[esq] <= pivo:
            esq += 1
        while dir >= 0 and V[dir] > pivo:
            dir -= 1
        if esq < dir:
            troca(V, esq, dir)

    V[inicio] = V[dir]
    V[dir] = pivo
    return dir

def quicksort(V, inicio, fim):
    if fim > inicio:
        pivo = particiona(V, inicio, fim)
        quicksort(V, inicio, pivo - 1)
        quicksort(V, pivo + 1, fim)

if __name__ == "__main__":
    v = [7, 8, 5, 6, 3, 4, 1, 2]
    n = len(v)

    quicksort(v, 0, n - 1)

    print("Array ordenado:", v)


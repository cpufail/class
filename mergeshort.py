def merge(v, ini, meio, fim):
    tam = fim - ini + 1
    temp = [0] * tam
    p1 = ini
    p2 = meio + 1
    fim1 = fim2 = 0

    for i in range(tam):
        if not fim1 and not fim2:
            if p1 <= meio and (p2 > fim or v[p1] < v[p2]):
                temp[i] = v[p1]
                p1 += 1
            else:
                temp[i] = v[p2]
                p2 += 1

            if p1 > meio:
                fim1 = 1
            if p2 > fim:
                fim2 = 1
        else:
            if not fim1:
                temp[i] = v[p1]
                p1 += 1
            else:
                temp[i] = v[p2]
                p2 += 1

    for j in range(tam):
        v[ini + j] = temp[j]

def mergesort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        mergesort(v, ini, meio)
        mergesort(v, meio + 1, fim)
        merge(v, ini, meio, fim)


def testemerg():
    v = [8, 7, 3, 4, 1, 9, 10]
    print("Lista original:", v)  

    mergesort(v, 0, len(v) - 1)
    print("Lista ordenada:", v)

testemerg()

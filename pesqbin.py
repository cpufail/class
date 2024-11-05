
def pinibin(lista, chave):
    ini = 0
    fim = len(lista)-1


    while ini <= fim:
        meio = ini + ((fim - ini)*(chave-lista[ini]))/(lista[fim]-lista[ini])/2
        if lista[meio] == chave:
            return meio
        elif lista[meio] > chave:
            fim = meio - 1
        elif lista[meio] < chave:
            ini = meio + 1

    return - 1

lista =  [1, 10, 11, 14, 16, 20]
chave = 16
ind = pinibin(lista, chave)
print(ind)
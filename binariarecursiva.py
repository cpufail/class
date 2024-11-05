def pesquisa_binaria(lista, primeiro, ultimo, valpesq):
    if ultimo >= primeiro:
       
        indimeio = (primeiro + ultimo) // 2
        elemento_do_meio = lista[indimeio]
       
 
        if elemento_do_meio == valpesq:
            return f"{elemento_do_meio} encontrado na posição {indimeio}"
 
        elif elemento_do_meio > valpesq:
            nova_posicao = indimeio - 1
            return pesquisa_binaria(lista, primeiro, nova_posicao, valpesq)
 
        elif elemento_do_meio < valpesq:
            nova_posicao = indimeio + 1
            return pesquisa_binaria(lista, nova_posicao, ultimo, valpesq)
 
    else:
        return "Não aparece na lista"
       
lista = [ 2, 5, 7, 10, 20, 30, 40 ]
pesquisar = 30
primeiro = 0
ultimo= len(lista) - 1
 
print(pesquisa_binaria(lista,primeiro,ultimo,pesquisar))
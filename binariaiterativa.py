def pesquisa_binaria(lista , valpesq):
    primeiro = 0
    tamanho = len(lista)
    ultimo = tamanho - 1
    indicemeio = (primeiro + ultimo) // 2
    elemento_do_meio = lista[indicemeio]

    encontrado = True
    while encontrado:
        if primeiro == ultimo:
            if elemento_do_meio != valpesq:
                encontrado = False
                return "Não aparece na lista"

        elif elemento_do_meio == valpesq:
            return f"{elemento_do_meio} encontrado na posição {indicemeio}"

        elif elemento_do_meio > valpesq:
            nova_posicao = indicemeio - 1
            ultimo = nova_posicao
            indicemeio = (primeiro + ultimo) // 2
            elemento_do_meio = lista[indicemeio]
            if elemento_do_meio == valpesq:
                return f"{elemento_do_meio} encontrado na posição {indicemeio}"

        elif elemento_do_meio < valpesq:
            nova_posicao = indicemeio + 1
            primeiro = nova_posicao
            ultimo = tamanho - 1
            indicemeio = (primeiro + ultimo) // 2
            elemento_do_meio = lista[indicemeio]
            if elemento_do_meio == valpesq:
                return f"{elemento_do_meio} encontrado na posição {indicemeio}"



lista = [10, 20, 30, 40, 50, 60, 70]
print(pesquisa_binaria(lista , 1000))
print(pesquisa_binaria(lista , 10))
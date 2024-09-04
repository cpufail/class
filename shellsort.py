def shellsort(arr, inicio, troca):
    for i in range(inicio + troca, len(arr), troca):
        valor_atual = arr[i]
        posicao = i

        while posicao >= troca and arr[posicao - troca] > valor_atual:
            arr[posicao] = arr[posicao - troca]
            posicao -= troca

        arr[posicao] = valor_atual

def shell_sort(arr):
    n = len(arr)
    contagem_sublistas = n // 2

    while contagem_sublistas > 0:
        for posicao_inicio in range(contagem_sublistas):
            shellsort(arr, posicao_inicio, contagem_sublistas)

        print(f"Após incrementos de tamanho {contagem_sublistas}, a lista é: {arr}")
        contagem_sublistas //= 2  

if __name__ == "__main__":
    minha_lista = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    print("Lista antes da ordenação:", minha_lista)
    shell_sort(minha_lista)
    print("Lista após a ordenação:", minha_lista)

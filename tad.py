class Lista:
    def __init__(self,info=None):
        self.info = info
        self.prox = None


def cria_lista():
    return Lista()


def insere_lista(lst, valor):
    novo = Lista(valor)
    novo.prox = lst
    return novo 

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox


def lista_vazia(lst):
    return lst is None

def lista_busca(lst,valor):
    atual = lst
    while atual is not None:
        if atual.info == valor:
            return atual
        atual = atual.prox
    return False

def lista_retirada(lst, valor):
    atual = lst
    ant = None
    while atual is not None:
        if atual.info == valor:
            if ant is None:
                lst = atual.prox
            else:
                ant.prox=atual.prox
            return lst
        ant = atual
        atual = atual.prox 
    return lst
 







lst = cria_lista()
lst = insere_lista(lst, 1)
lst = insere_lista(lst, 2)
lst = insere_lista(lst, 3)
lst = insere_lista(lst, 4)    
lista_imprime(lst)


# Busca um elemento
valor_busca = 3
resultado_busca = lista_busca(lst, valor_busca)
print(f"\nElemento {valor_busca} encontrado:", resultado_busca.info if resultado_busca else "Não encontrado")

# Retira um elemento
lista = lista_retirada(lst, 4)
print("Lista após retirar o elemento 4:")
lista_imprime(lista)

# Retira todos os elementos com valor 10
lista = lista_retirada(lista, 1)
print("\nLista após retirar todos os elementos com valor 1:")
lista_imprime(lista)


class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir(self, chave, valor):
        novo_no = No(chave, valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def remover(self, chave):
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.chave == chave:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def obter(self, chave):
        atual = self.cabeca
        while atual:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        return None

    def obter_todos(self):
        valores = []
        atual = self.cabeca
        while atual:
            valores.append((atual.chave, atual.valor))
            atual = atual.proximo
        return valores
     
class hashencad:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [ListaEncadeada() for _ in range(tamanho)]

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        self.tabela[indice].inserir(chave, valor)

    def remover(self, chave):
        indice = self._hash(chave)
        return self.tabela[indice].remover(chave)

    def obter(self, chave):
        indice = self._hash(chave)
        return self.tabela[indice].obter(chave)

    def __str__(self):
        return {i: self.tabela[i].obter_todos() for i in range(self.tamanho)}.__str__()

tabela_hash = hashencad()
tabela_hash.inserir('chave1', 'valor1')
tabela_hash.inserir('chave2', 'valor2')
tabela_hash.inserir('chave1', 'valor3')
print(tabela_hash)
print(tabela_hash.obter('chave1'))
tabela_hash.remover('chave1')
print(tabela_hash)
class Arquivo:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho

class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]  # Lista de listas para encadeamento separado

    def funcao_hash(self, nome):
        return hash(nome) % self.tamanho

    def adicionar(self, arquivo):
        indice = self.funcao_hash(arquivo.nome)
        for a in self.tabela[indice]:
            if a.nome == arquivo.nome:  # Evitar duplicatas
                return
        self.tabela[indice].append(arquivo)

    def buscar(self, nome):
        indice = self.funcao_hash(nome)
        for a in self.tabela[indice]:
            if a.nome == nome:
                return a
        return None

    def remover(self, nome):
        indice = self.funcao_hash(nome)
        for i, a in enumerate(self.tabela[indice]):
            if a.nome == nome:
                del self.tabela[indice][i]
                return True
        return False

    def listar(self):
        arquivos = []
        for lista in self.tabela:
            arquivos.extend(lista)
        return arquivos
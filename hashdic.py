class TabelaHash:
    def __init__(self):
        self.tabela = {}
    def inserir(self, chave, valor):
        if chave not in self.tabela:
            self.tabela[chave] = []
        self.tabela[chave].append(valor)
    def obter(self, chave):
        return self.tabela.get(chave, [])
    def remover(self, chave, valor):
        if chave in self.tabela:
            try:
                self.tabela[chave].remove(valor)
            except ValueError:
                pass
    def __str__(self):
        return str(self.tabela)

tabela_hash = TabelaHash()
tabela_hash.inserir('chave1', 'valor1')
tabela_hash.inserir('chave1', 'valor2')
tabela_hash.inserir('chave2', 'valor3')
print(tabela_hash)
tabela_hash.remover('chave1', 'valor1')
print(tabela_hash)
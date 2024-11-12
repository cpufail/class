class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.esquerda = None
        self.direita = None

class ABB:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        self.raiz = self._inserir_recursivo(self.raiz, produto)

    def _inserir_recursivo(self, no, produto):
        if no is None:
            return Produto(produto.id, produto.nome, produto.descricao, produto.preco)
        
        if produto.id < no.id:
            no.esquerda = self._inserir_recursivo(no.esquerda, produto)
        elif produto.id > no.id:
            no.direita = self._inserir_recursivo(no.direita, produto)
        
        return no

    def buscar(self, id):
        return self._buscar_recursivo(self.raiz, id)

    def _buscar_recursivo(self, no, id):
        if no is None or no.id == id:
            return no
        
        if id < no.id:
            return self._buscar_recursivo(no.esquerda, id)
        else:
            return self._buscar_recursivo(no.direita, id)

    def remover(self, id):
        self.raiz = self._remover_recursivo(self.raiz, id)

    def _remover_recursivo(self, no, id):
        if no is None:
            return no
        
        if id < no.id:
            no.esquerda = self._remover_recursivo(no.esquerda, id)
        elif id > no.id:
            no.direita = self._remover_recursivo(no.direita, id)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                minimo = self._encontrar_minimo(no.direita)
                no.id = minimo.id
                no.nome = minimo.nome
                no.descricao = minimo.descricao
                no.preco = minimo.preco
                no.direita = self._remover_recursivo(no.direita, minimo.id)

        return no

    def _encontrar_minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

    def listar_ordem_crescente(self):
        produtos = []
        self._listar_ordem_crescente_recursivo(self.raiz, produtos)
        return produtos

    def _listar_ordem_crescente_recursivo(self, no, produtos):
        if no is not None:
            self._listar_ordem_crescente_recursivo(no.esquerda, produtos)
            produtos.append(no)
            self._listar_ordem_crescente_recursivo(no.direita, produtos)

# Exemplo de uso:

arvore = ABB()

produto1 = Produto(30, "Produto A", "Descrição A", 100.0)
produto2 = Produto(20, "Produto B", "Descrição B", 50.0)
produto3 = Produto(40, "Produto C", "Descrição C", 150.0)

arvore.inserir(produto1)
arvore.inserir(produto2)
arvore.inserir(produto3)

produto = arvore.buscar(20)
if produto:
    print(f"Produto encontrado: {produto.nome} - {produto.preco} R$")

arvore.remover(20)
produtos = arvore.listar_ordem_crescente()
for p in produtos:
    print(f"ID: {p.id} | Nome: {p.nome} | Preço: {p.preco} R$")

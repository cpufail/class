# Definição das classes
class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos  # Lista de gêneros

class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None
 
class ArvoreJogos:
    def __init__(self):
        self.raiz = None

    def inserir(self, jogo):
        if self.raiz is None:
            self.raiz = NoJogo(jogo)
        else:
            self._inserir_recursivo(self.raiz, jogo)

    def _inserir_recursivo(self, no_atual, jogo):
        if jogo.preco < no_atual.jogo.preco:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoJogo(jogo)
            else:
                self._inserir_recursivo(no_atual.esquerda, jogo)
        else:
            if no_atual.direita is None:
                no_atual.direita = NoJogo(jogo)
            else:
                self._inserir_recursivo(no_atual.direita, jogo)

    def buscar_por_preco(self, preco):
        return self._buscar_por_preco_recursivo(self.raiz, preco)

    def _buscar_por_preco_recursivo(self, no_atual, preco):
        if no_atual is None:
            return []
        jogos = []
        if no_atual.jogo.preco == preco:
            jogos.append(no_atual.jogo)
        jogos += self._buscar_por_preco_recursivo(no_atual.esquerda, preco)
        jogos += self._buscar_por_preco_recursivo(no_atual.direita, preco)
        return jogos

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        return self._busca_por_faixa_preco_recursivo(self.raiz, preco_minimo, preco_maximo)

    def _busca_por_faixa_preco_recursivo(self, no_atual, preco_minimo, preco_maximo):
        if no_atual is None:
            return []
        jogos = []
        if preco_minimo <= no_atual.jogo.preco <= preco_maximo:
            jogos.append(no_atual.jogo)
        jogos += self._busca_por_faixa_preco_recursivo(no_atual.esquerda, preco_minimo, preco_maximo)
        jogos += self._busca_por_faixa_preco_recursivo(no_atual.direita, preco_minimo, preco_maximo)
        return jogos

class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = {}

    def adicionar_jogo(self, jogo):
        for genero in jogo.generos:
            if genero not in self.genero_para_jogos:
                self.genero_para_jogos[genero] = []
            self.genero_para_jogos[genero].append(jogo.jogo_id)

    def obter_jogos(self, genero):
        return self.genero_para_jogos.get(genero, [])

class MotorBuscaJogos:
    def __init__(self):
        self.catalogo_jogos = ArvoreJogos()
        self.generos = HashGeneros()

    def adicionar_jogo(self, jogo):
        self.catalogo_jogos.inserir(jogo)
        self.generos.adicionar_jogo(jogo)

    def buscar_por_preco(self, preco):
        return self.catalogo_jogos.buscar_por_preco(preco)

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        return self.catalogo_jogos.busca_por_faixa_preco(preco_minimo, preco_maximo)

    def buscar_por_genero(self, genero):
        return self.generos.obter_jogos(genero)

# Dados dos jogos
jogos = [
    Jogo(1, "The Legend of Zelda: Breath of the Wild", "Nintendo", 300, ["Aventura"]),
    Jogo(2, "The Witcher 3: Wild Hunt", "CD Projekt Red", 150, ["RPG"]),
    Jogo(3, "Minecraft", "Mojang", 120, ["Sandbox"]),
    Jogo(4, "Red Dead Redemption 2", "Rockstar Games", 200, ["Ação"]),
    Jogo(5, "GTA V", "Rockstar Games", 100, ["Ação"]),
    Jogo(6, "Dark Souls III", "FromSoftware", 180, ["RPG de Ação"]),
    Jogo(7, "Cyberpunk 2077", "CD Projekt Red", 220, ["RPG"]),
    Jogo(8, "God of War (2018)", "Santa Monica Studio", 200, ["Ação"]),
    Jogo(9, "Hollow Knight", "Team Cherry", 60, ["Metroidvania"]),
    Jogo(10, "Among Us", "Innersloth", 10, ["Party Game"]),
]

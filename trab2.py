from dados_jogos import jogos, MotorBuscaJogos

if __name__ == "__main__":
    # Criando o motor de busca
    motor_busca = MotorBuscaJogos()

    # Adicionando jogos ao motor de busca
    for jogo in jogos:
        motor_busca.adicionar_jogo(jogo)

    # Buscando jogos com preço menor que R$100
    print("Buscando jogos com preço menor que R$100:")
    jogos_menor_100 = [jogo for jogo in jogos if jogo.preco < 100]
    for jogo in jogos_menor_100:
        print(f"- {jogo.titulo} ({jogo.preco} R$)")

    # Buscando jogos por faixa de preço
    print("\nBuscando jogos maiores que R$100:")
    jogos_faixa = motor_busca.busca_por_faixa_preco(101, 1000)
    for jogo in jogos_faixa:
        print(f"- {jogo.titulo} ({jogo.preco} R$)")

    # Buscando jogos por gênero
    print("\nBuscando jogos do gênero 'Ação':")
    jogos_genero_acao = motor_busca.buscar_por_genero("Ação")
    for jogo_id in jogos_genero_acao:
        for jogo in jogos:
            if jogo.jogo_id == jogo_id:
                print(f"- {jogo.titulo} ({jogo.preco} R$)")

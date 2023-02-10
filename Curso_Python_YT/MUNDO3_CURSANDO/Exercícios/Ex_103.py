def ficha(nome="",gols=''):
    """
    --> Imprime ficha de um jogador
    :para nome: Imprime o nome do jogador
    :para gols: Quantidade de gols feitos
    :return: retorna a impressão de nome + gols"""
    print(f'O jogador {nome if nome != "" else "<desconhecido>"} fez {int(gols) if gols.isnumeric() == True else "0"} gol(s) no campeonato.')

ficha(str(input('Nome do Jogador: ')).strip(),str(input('Número de Gols: ')))

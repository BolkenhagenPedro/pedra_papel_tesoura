from random import choice
from os import linesep

def limpar_terminal():
    try:
        from os import system
        from platform import system as sys
        
        sistema_operacional = sys()
        
        if sistema_operacional == 'Windows': system('cls')
        elif sistema_operacional == 'Linux': system('clear')
        elif sistema_operacional == 'Darwin': system('clear')

    except:
        return False

def sistema_ranking(vencidas, empatadas, perdidas, total_partidas, nome):
    escrever = f"{nome} jogou {total_partidas}, ganhou {vencidas}, empatou {empatadas} e perdeu {perdidas}"
    return escrever

def ranking():
    with open('ranking.txt', 'r') as file:
        print('=' * 30)
        for linha in file:
            print(linha, end='')
        print('=' * 30)


# Definições das listas
# Lista de escolhas para o bot e para verificar se o jogador digitou uma jogada corretamente     
escolhas = ['pedra', 'papel', 'tesoura']

nome = input(f'Informe o nome de jogador: ').strip().title()
while True:
    with open('ranking.txt', 'r') as file:
        for linha in file:
            while nome in linha:
                print('Este nome existe ou é inpróprio!')
                nome = input(f'Informe o nome de jogador: ').strip()
    break

input('Aperte enter para começar...')
limpar_terminal()
# Contadores
vencidas = perdidas = empatadas = total = 0
venceu = False

while True:
    while True:
        # Jogada do Bot
        jogada_bot = choice(escolhas)

        # Jogada do jogador
        jogada_player = input(f'{nome} informe sua jogada --> tesoura | papel | pedra: ').strip().lower()
        while jogada_player not in escolhas:
            print('Digite uma jogada válida!')
            jogada_player = input(f'{nome} informe sua jogada --> tesoura | papel | pedra: ').strip().lower()
        limpar_terminal()
        # Se a jogada do jogador for pedra
        if jogada_player == 'pedra':

            # Se o jogador empatou
            if jogada_bot == 'pedra':
                print(f'Empate! O bot jogou {jogada_bot} e {nome} jogou {jogada_player}.')
                empatadas += 1

            # Se o jogador perdeu
            elif jogada_bot == 'papel':
                print(f'Perdeu! O bot jogou {jogada_bot} e {nome} jogou {jogada_player}.')
                perdidas += 1

            # Se o jogador ganhou
            else:
                print(f'Ganhou! O bot jogou {jogada_bot} e {nome} jogou {jogada_player}.')
                vencidas += 1
                venceu = True


        # Se o jogador jogou papel
        elif jogada_player == 'papel':

            # Se o jogador empatou
            if jogada_bot == 'papel':
                print(f'Empate! O bot jogou {jogada_bot} e {nome} jogou {jogada_player}.')
                empatadas += 1

            # Se o jogador perdeu
            elif jogada_bot == 'tesoura':
                print(f'Perdeu! O bot jogou {jogada_bot} e {nome} jogou {jogada_player}.')
                perdidas += 1

            # Se o jogador ganhou
            else:
                print(f'Ganhou! O bot jogou {jogada_bot} e {nome} jogou {jogada_player}.')
                vencidas += 1
                venceu = True

        # Se o jogador jogou tesoura
        else:
        
            # Se o jogador empatou
            if jogada_bot == 'tesoura':
                print(f'Empate! O bot jogou {jogada_bot} e {nome} jogou {jogada_player}.')
                empatadas += 1

            # Se o jogador perdeu
            elif jogada_bot == 'pedra':
                print(f'Perdeu! O bot jogou {jogada_bot} e {nome} jogou {jogada_player}.')
                perdidas += 1

            # Se o jogador ganhou
            else:
                print(f'Ganhou! O bot jogou {jogada_bot} e {nome} jogou {jogada_player}.')
                vencidas += 1
                venceu = True

        
        total += 1
        if venceu:
            resp = input('Quer continuar? (S/N) ').lower().strip()[0]
            while resp not in ['s', 'n']:
                print('Digite um resposta válida!')
                resp = input('Quer continuar? (S/N) ').lower().strip()[0]
            
            if resp == 'n':
                with open('ranking.txt', 'a', newline='') as file:
                    file.write(sistema_ranking(vencidas, empatadas, perdidas, total, nome) + linesep)
                    break
            venceu = False

    print('[Selecione uma opção]')
    print('[1] - Novo Jogador')
    print('[2] - Mostrar Histórico de jogadores')
    print('[3] - Sair')
    resp = int(input('Digite uma opção: '))
    while resp not in [1, 2, 3]:
        print('Digite uma opção correta!')
        resp = int(input('Digite uma opção: '))
    if resp == 3: break
    elif resp == 2: 
        ranking()

    else:
        nome = input(f'Informe o nome de jogador: ').strip().title()
        while True:
            with open('ranking.txt', 'r') as file:
                for linha in file:
                    while nome in linha:
                        print('Este nome existe ou é inpróprio!')
                        nome = input(f'Informe o nome de jogador: ').strip()
            break
        vencidas = perdidas = empatadas = total = 0
        venceu = False
        limpar_terminal()
        continue

    print('[Selecione uma opção]')
    print('[1] - Novo Jogador')
    print('[2] - Sair')
    resp = int(input('Digite uma opção: '))
    while resp not in [1, 2]:
        print('Digite uma opção correta!')
        resp = int(input('Digite uma opção: '))
    if resp == 2: break
    nome = input(f'Informe o nome de jogador: ').strip().title()
    while True:
        with open('ranking.txt', 'r') as file:
            for linha in file:
                while nome in linha:
                    print('Este nome existe ou é inpróprio!')
                    nome = input(f'Informe o nome de jogador: ').strip()
        break
    vencidas = perdidas = empatadas = total = 0
    venceu = False
    limpar_terminal()
    continue
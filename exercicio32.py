# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randrange
cont = 0
print('\033[1;35m------IMPAR OU PAR------\033[m')
while True:
    pc = randrange(0, 10)
    n = int(input('Diga um Valor: '))
    soma = pc + n
    print('=' * 20)
    op = ' '
    while op not in 'PI':
        op = str(input('PAR ou IMPAR [P/I]: ')).strip().upper()[0]
    if op in 'Pp':
        if soma % 2 == 0:
            print(f'voce jogou {n} e o pc {pc}. o Total deu {soma} deu PAR')
            print('=' * 20)
            print('\033[1;34mVOCE VENCEU')
            print('VAMOS JOGAR NOVAMETNE...\033[m')
            print('=' * 20)
        else:
            print(f'Voce jogou {n} e o pc {pc}.o total deu {soma} deu IMPAR')
            print('o Computador venceu')
            break
    elif op in 'Ii':
        if soma % 2 != 0:
            print(f'Voce jogou {n} e o pc {pc}.o total deu {soma} deu IMPAR')
            print('=' * 20)
            print('\033[1;31mVoce venceu')
            print('Vamo jogar novamente...\033[m')
            print('=' * 20)
        else:
            print(f'voce jogou {n} e o pc {pc}. o Total deu {soma} deu PAR')
            print('o computador venceu')
            break
    cont += 1
print(f'Game over ! voce venceu {cont} vezes')
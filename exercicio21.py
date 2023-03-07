''' Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar
 mostrando no final quantos palpites foram necessários para vencer.'''
from random import randrange
num = randrange(0, 10)
print('\033[1;31m{:-^40}\033[m'.format('JOGO DE ADVINHA'))
print('''\033[1;34mSou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?\033[m''')
palpite = int(input('Qual o seu palpite?'))
cont = 1
while palpite != num:
    if palpite < num:
        print('\033[1;32mMais... tente mais uma vez.\033[m')
    else:
        print('\033[1;36mMenos... Menos, tente mais uma vez.\033[m')
    palpite = int(input('Qual o seu palpite:'))
    cont += 1
print('\033[1;35mVocê acertou com {} tentativas, párabens\033[m'.format(cont))


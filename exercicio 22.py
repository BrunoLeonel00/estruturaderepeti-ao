# Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
num1 = int(input('Digite um numero:'))
num2 = int(input('digite mais um numero:'))
g = 0
while g < 2:
    print(('''\033[1;36m[{:^3}] soma'
[{:^3}] Multiplicar
[{:^3}] maior 
[{:^3}]novos numeros
[{:^3}] encerre o programa\033[m''').format(1, 2, 3, 4, 5))
    op = int(input('>>> Qual a sua opção?'))
    if op == 1:
        print('A soma de {} e {} é {}'.format(num1, num2, num1 + num2))
    elif op == 2:
        print('O resultado de {} X {} é {}'.format(num1, num2, num1 * num2))
    elif op == 3:
        if num1 < num2:
            print('entre {} e {} o número com maior valor é {}'.format(num1, num2, num2))
        else:
            print('entre {} e {} o número com maior valor é {}'.format(num1, num2, num1))
    elif op == 4:
        print('Resetando...')
        print('Informe os novos valores.')
        num1 = int(input('digite um numero:'))
        num2 = int(input('digite mais um numero:'))
    elif op == 5:
        print('fim dp programa,volte sempre')
        exit()
    else:
        print('Opçao invalida, digite novamente')
    print('=' * 30)
    sleep(1)


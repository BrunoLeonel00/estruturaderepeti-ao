#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Gerador de P.A')
print('-='* 10)
termo = int(input('primeiro termo:'))
razao = int(input('razap da PA: '))
d = 1
while d <= 10:
    print(termo, end= '')
    print(' -> ' if d < 10 else ' FIM', end='' )
    termo += razao
    d = d + 1

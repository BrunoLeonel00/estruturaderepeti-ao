# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
print('---- LOJA DO BRUNO----')
totC = prod = prodB = menor = 0
barato = ''
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    mais = ' '
    totC += preco
    menor += 0
    while mais not in 'SN':
        mais = str(input('Quer continuar a compra? [S/N] ')).strip().upper()[0]
    if preco >= 1000:
        prod += 1
    if menor == 0:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    if mais == 'N':
        break
print('{:-^40}'.format('fim do programa'))
print(f'o Total a pagar é de R${totC:.2f}')
print(f'{prod} produtos acima de R$ 1000 ')
print(f'O produto mais barato é {barato}  e seu preço é de R$ {menor}')

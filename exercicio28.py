mais = 'S'
cont = soma = maior = menor = 0
while mais in 'Ss':
    num = int(input('digite um número:'))
    cont += 1
    soma += num
    mais = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('Você digitou {} numeros e a media entre eles é {}'.format(cont, media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))


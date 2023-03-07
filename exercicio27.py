cont = 0
conta = 0
soma = 0
while cont < 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        conta += 1
        soma += n
    else:
        cont = n
print('Você digitou {} numeros e a soma entre eles é {}'.format(conta, soma))


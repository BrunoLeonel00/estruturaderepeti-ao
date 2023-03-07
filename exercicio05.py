#Faça um programa que leia 6 números inteiros,e mostre a soma daqueles que forem pares
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} numero:'.format(c)))
    if num % 2 == 0:
        cont = cont + 1
        soma = num + soma
print('Nessa lista {} sao pares, e a soma entre eles é igual a {}'.format(cont, soma))

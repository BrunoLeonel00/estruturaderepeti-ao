#Faça um programa que calcule a soma de todos os números multiplos de 3 e que se encontram no intervalo de 1 a 500
soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('a soma de todos os {} é igual a {}'.format(cont, soma))

#'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = str(input('informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor, informe seu sexo:')).strip().upper()[0]
cont = str(input('podemos contiunar a validação? [S/N]')).strip().upper()[0]
if cont == 'S':
    idade = int(input('informe sua idade:'))
    if idade != 18:
        print('Voce precisa ter no minimo 18 anos para continuar')
        exit()

print('Sexo {} registrado com sucesso'.format(sexo))
print('idade {} resgistrada com sucesso'.format(idade))

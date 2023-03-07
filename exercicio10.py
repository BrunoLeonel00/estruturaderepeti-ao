#'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos'''
soma = 0
lista = []
cont = 0
for dados in range(1, 5):
    print('{:-^10}'.format(dados))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma = soma + idade
    media = soma / 4
    if Sexo == 'M':
        lista.append(idade)
    if Sexo == 'F' and idade < 20:
        cont += 1
print(' A média de idade do grupo é de {:.1f}'.format(media))
print(' O Homem mais velho tem {} anos '.format(max(lista)))
print(' A o Todo temos {} com meno de 20 anos'.format(cont))














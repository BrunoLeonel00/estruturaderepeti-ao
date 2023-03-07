from datetime import date
cont = 0
cont1 = 0
for c in range(1, 8, 1):
    ano = int(input('Em que ano a {} pessoa nasceu?'.format(c)))
    maior_idade = date.today().year - ano
    if maior_idade >= 18:
        cont += 1
    else:
        cont1 += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
print('e tivemos {} pessoa menores de idade'.format(cont1))


tot = homem = mulher = 0
while True:
    print('----CADASTRE UMA PESSOA----')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        tot += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if mais == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: \033[1;36m{tot}\033[m')
print(f'Ao todo temos \033[1;36m{homem}\033[m homens cadastrados')
print(f'temos \033[1;36m{mulher}\033[m mulheres com menos do 20 anos')









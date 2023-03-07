#'''Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd
soma = 0
contM = 0
for pess in range(1, 3):
    print('----{} Pessoa ----'.format(pess))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    salario = float(input('Salario:R$'))
    sexo = str(input('Sexo [M/F]:')).strip()
    estado = str(input('Estado Civil:')).strip()
    soma += salario
    media = soma / 2







#desenvolva um programa  que leia o primeiro termo e a razão de um PA, no final mostre os dez primeiros termos dessa progracão
print('{:=^40}'.format('\033[1;34m10 TERMOS DE UMA PA\033[m'))
n = int(input('primeiro termo:'))
r = int(input('razão:'))
for c in range(1, 11):
    print(n + (c - 1) * r, end=' -> ')
print('ACABOU')

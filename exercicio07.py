num = int(input('digite um número:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0: #se o resto da divisao for igual a 0, some as variaveis
        tot += 1
if tot == 2: #so pode ter dois divisores (1 e ele mesmo )
    print('o numero {} é primo '.format(num))
else:
    print('o numero {} nao é primo'.format(num))





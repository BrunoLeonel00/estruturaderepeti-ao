#Sequência de fibonacci
print('-=' * 10)
print('SequÊncia de Fibonacci')
print('-=' * 10)
op = int(input('quantos termos voce quer mostar ?'))
 # Como o valor do primeiro termo e seundo sempre sera 0 e 1, ja atribuimos as variaveis
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3  # ja sabemos o valor de t3, deixamos o contador em 3
while cont <= op:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3  # fazemos o t1 receber o t2, e o t2 receber o t3.Para dar continuidade a sequência
    cont += 1
print(' -> FIM')


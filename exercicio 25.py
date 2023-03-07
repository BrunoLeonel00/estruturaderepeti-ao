#aprimoramento do código anterior
print(' CONTADOR DE PA')
print('-=' * 10)
termo = int(input('informe o primeiro termo: '))
razao = int(input('informe a razãp: '))
d = 1
conta = 0
while d <= 10:
    print(termo, end=' -> ')
    termo += razao
    d += 1
    conta += 1 #mesma base
print('Pausa...')
cont = 1
while cont != 0: # enquanto o usuario nao digitar o número 0, o loop vai continuar
    cont = int(input('\nQuantos termos deseja mostrar a mais?'))
    if cont >= 1:
        d = 0
        while d < cont:   # ira se repetir até a variavel D chegar na mesma quantiade da variavel CONT
            print(termo, end=' -> ')
            termo += razao
            d += 1
            conta += 1 #contADOR
        print('pausa...\n')
    else:
        print('progressao finalizada com {} termos mostrados.'.format(conta))



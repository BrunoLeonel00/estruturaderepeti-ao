soma = cont = 0
while True:
    n = int(input('digite um numero [Digite 999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f' a soma dos {cont} numeros é {soma}')

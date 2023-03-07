#fatorial
print('Calculando fatorial')
num = (int(input('digite um numero:')))
mult = 1
print('calculando {}! = '.format(num), end='')
while num != 0:
    print('{} '.format(num), end='')
    print('x ' if num > 1 else '= ', end='')
    mult *= num
    num -= 1
print('{}'.format(mult))



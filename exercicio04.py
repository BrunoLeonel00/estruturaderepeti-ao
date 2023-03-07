#tabuada
num = int(input('digite um numero para ver sua tabuada:'))
for c in range(1, 11):
    print('{} X {:^2} = {}'.format(num, c, num * c))


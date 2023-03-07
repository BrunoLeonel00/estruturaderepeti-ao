# tabuada 3.0
m = 1
while True:
    print('-=' * 10)
    n = int(input('Quer ver a tabuada de qual valor?:'))
    print('-=' * 10)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'\033[1;36m{n} x {m:^2} = {n * m}\033[m')
        m += 1
print('\033[1;31mprograma de taubada encerrado\033[m')

#numeros impares
num = int(input('digite um número:'))
x = 0
while x <= num:
    if x % 3 == 0:
        print(x)
    x = x + 3

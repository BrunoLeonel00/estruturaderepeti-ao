for c in range(0, 2):
    frase = str(input('digite uma frase:')).strip().upper()
    frase1 = frase.replace(' ', '') #tira os espaços
    inverso = frase[::-1].replace(' ', '') # invere a frase, sem s espoços
    if frase1 == inverso:
        print('o inverso de  {} é {}'.format(frase, inverso))
        print('\033[1;34mtemos um POLINDROMO\033[m')
    elif frase != inverso:
        print('a frase {} \033[1;31mnao é um polindromo\033[m'.format(frase))
print('obrigado')


num1 = int(input('Insira o primeiro numero: '))
num2 = int(input('Insira o segundo numero: '))

if (num1 > num2):
    print('O primeiro numero eh maior que o segundo numero, pois {} eh maior que {}.'.format(num1, num2, num1, num2))
elif (num2 > num1):
    print('O segundo numero eh maior que o primeiro numero, pois {} eh maior que {}.'.format(num2, num1, num2, num1))
else:
    print('Nao existe valor maior, pois {} eh igual a {}'.format(num1, num2))

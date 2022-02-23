from math import pow, sqrt

oposto = float(input('Insira o cateto oposto: '))

adjacente = float(input('Insira o cateto adjacente: '))

hipotenusa = sqrt(pow(oposto,2) + pow(adjacente,2))

print('A hipotenusa desse triangulo eh {:.2f}!'.format(hipotenusa))

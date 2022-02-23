salario = float(input('Insira o salario atual do trabalhador: '))

aumento = salario * 0.15

salario2 = salario + aumento

print('O novo salario do trabalhador sera de R${:.2f}! Um aumento de R${:.2f}'.format(salario2, aumento))

salario = float(input('Insíra o salário do trabalhador: '))

if (salario <= 1250):
    aumento: float = salario * 0.15
    print('O novo salário do funcionário será de R${:.2f}. Um aumento de R${:.2f}, ou 15%!'.format(salario+aumento, aumento))
else:
    aumento: float = salario * 0.10
    print('O novo salário do funcionário será de R${:.2f}. Um aumento de R${:.2f}, ou 10%!'.format(salario+aumento, aumento))

salario = float(input('Insíra o valor do seu salário atual: '))
casa = float(input('Insíra o valor do imóvel que deseja comprar: '))
anos = int(input('Insíra em quantos anos deseja parcelar esse imóvel: '))

valor_parcela = casa / anos / 12
comprometido = valor_parcela * 100 / salario

if valor_parcela <= salario * 0.3:
    print('O valor da sua parcela será de R${:.2f}! Com isso você estará comprometendo {:.1f}% do seu salário. Parabéns! Seu financiamento foi aprovado!'.format(valor_parcela, comprometido))
else:
    print('O valor da sua parcela será de R${:.2f}! Com isso você estará comprometendo {:.1f}% do seu salário. Infelizmente não podemos aprovar um financiamento para você nesse momento.'.format(valor_parcela, comprometido))



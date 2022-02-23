dias = int(input('Por quantos dias o carro ficou alugado? '))

km = float(input('Quantos quilometros o carro percorreu? '))

preco = (dias * 60) + (km * 0.15)

print ('O valor a ser pago eh de R${:.2f}!'.format(preco))

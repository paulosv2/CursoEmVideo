preco = float(input('insira o valor atual do produto: '))

desconto = preco * 0.05

preco2 = preco - desconto

print(f'Esse produto custa R${preco2} na promocao. Eh um desconto de R${desconto}!')

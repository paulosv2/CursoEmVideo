velocidade = float(input('Insíra a velocidade do carro: '))

if velocidade <= 80:
    print('{:.1f}Km/h! Limite permitido! Boa viagem!'.format(velocidade))
else:
    print('{:.1f}Km/h!!! Você está acima do limite permitido!!! Você recebeu uma multa no valor deR${:.1f}!!!'.format(velocidade, (velocidade-80)*7))


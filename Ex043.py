altura = float(input('Insíra sua altura, em metros: '))
peso = float(input('Insíra seu peso, em Kg: '))

imc = peso / pow(altura, 2)

print('Seu IMC é de: {:.2f}.'.format(imc))

if imc < 18.5:
    print('Seu peso está abaixo do ideal!')
elif imc < 25:
    print('Seu peso está ideal!')
elif imc < 30:
    print('Você está com sobrepeso!')
elif imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade morbida!!!')
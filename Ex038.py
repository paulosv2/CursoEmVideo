num1 = int(input('Insíra o primeiro número: '))
num2 = int(input('Insíra o segundo número: '))

if num1 < num2:
    print('O menor número é {} e o maior número é {}!'.format(num1, num2))
elif num2 < num1:
    print('O menor número é {} e o maior número é {}!'.format(num2, num1))
else:
    print('Esse números são iguais. Esse é o número {}!'.format(num1))

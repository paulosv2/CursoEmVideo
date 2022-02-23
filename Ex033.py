num1 = int(input('Insíra o primeiro número: '))
num2 = int(input('Insíra o segundo número: '))
num3 = int(input('Insíra o terceiro número: '))


if(num1>num2):
    if(num2>num3):
        print('O maior número é {} e o menor número é {}!'.format(num1, num3))
    elif(num3<num1):
        print('O maior número é {} e o menor número é {}!'.format(num1, num2))
    else:
        print('O maior número é {} e o menor número é {}!'.format(num3, num2))
else:
    if(num1>num3):
        print('O maior número é {} e o menor número é {}!'.format(num2, num3))
    elif(num3>num2):
        print('O maior número é {} e o menor número é {}!'.format(num3, num1))
    else:
        print('O maior número é {} e o menor número é {}!'.format(num2, num1))

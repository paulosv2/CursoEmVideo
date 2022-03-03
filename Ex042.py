lado1 = int(input('Insira o primeiro lado do triangulo: '))
lado2 = int(input('Insira o segundo lado do triangulo: '))
lado3 = int(input('insira o terceiro lado do triangulo: '))

if((lado1 + lado2) < lado3 or (lado2 + lado3) < lado1 or (lado1 + lado3 < lado2)):
    print('Infelizmente essas retas não podem formar um triângulo!')
else:
    if lado1 == lado2:
        if lado1 == lado3:
            print('Esse eh um triangulo equilatero, pois possui os 3 lados iguais!')
        else:
            print('Esse eh um triangulo isosceles, pois possui 2 lados iguais!')
    elif lado1 == lado3:
        print('Esse eh um triangulo isosceles, pois possui 2 lados iguais!')
    elif lado2 == lado3:
        print('Esse eh um triangulo isosceles, pois possui 2 lados iguais!')
    else:
        print('Esse eh um triangulo escaleno, pois nenhum lado eh igual ao outro!')

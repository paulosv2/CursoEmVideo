idade = int(input('Insira sua idade para saber de qual categoria voce faz parte: '))

if idade <= 9:
    print('Com {} anos sua categoria eh MIRIN!'.format(idade))
elif idade <= 14:
    print('Com {} anos sua categoria eh INFANTIL!'.format(idade))
elif idade <= 19:
    print('Com {} anos sua categoria eh JUNIOR!'.format(idade))
elif idade == 20:
    print('Com {} anos sua categoria eh SENIOR!'.format(idade))
else:
    print('Com {} anos sua categoria eh MASTER!'.format(idade))


ano = int(input('Insíra um ano qualquer para saber se ele é bissexto: '))

if ((ano % 4 == 0) and (ano % 100 != 0)):
    print('O ano {} é bissexto!'.format(ano))
else:
    if ano % 400 == 0:
        print('O ano {} é bissexto!'.format(ano))
    else:
        print('O ano {} não é bissexto!'.format(ano))

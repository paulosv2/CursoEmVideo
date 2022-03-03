nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Sua media eh {}. Infelizmente voce foi reprovado!'.format(media))
elif media < 7:
    print('Sua media eh {}. Voce esta de recuperacao!'.format(media))
else:
    print('Sua media eh {}. Parabens! Voce foi aprovado!'.format(media))

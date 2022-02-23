frase = input('Insíra a frase desejada: ').lower().strip()

print('A letra"A" aparece {} vezes nessa frase!'.format(frase.count('a')))
print('A letra "A" aparece pela primeira vez na posição {} e pela última vez na posição {}'.format(frase.find('a'), frase.rfind('a')))

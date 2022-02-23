
from random import choice
aluno1 = input('Insira o primeiro aluno: ')
aluno2 = input('Insira o segundo aluno: ')
aluno3 = input('Insira o terceiro aluno: ')
aluno4 = input('Insira o quarto aluno: ')

lista =[aluno1, aluno2, aluno3, aluno4]
sorteado = choice(lista)

print('O aluno sorteado foi {}!'.format(sorteado))

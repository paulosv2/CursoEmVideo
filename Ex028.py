from random import randint
from time import sleep
user = int(input("Insíra um número entre 0 e 5! "))

computador: int = randint(0,5)

print('PROCESSANDO...')
sleep(3)

if computador == user:
    print('Parabéns!Você venceu!')
else:
    print('O computador pensou no número {}! Você perdeu!'.format(computador))

ang = int(input('Insira o angulo: '))

from math import radians, sin, cos, tan
rad = radians(ang)

print('Seno de {} graus : {:.2f}'.format(ang, sin(rad)))
print('Coseno de {} graus : {:.2f}'.format(ang, cos(rad)))
print('Tangente de {} graus : {:.2f}'.format(ang, tan(rad)))

distancia = int(input('Insíra a distância da viagem a ser realizada: '))

if distancia <= 200:
    print('Uma viagem de {} Km custará R${}!'.format(distancia, distancia*0.5))
else:
    if distancia*0.45 > 100:
        print('Uma viagem de {} Km custará R${}!'.format(distancia, distancia*0.45))
    else:
        print('Uma viagem de {} Km custará R${}!'.format(distancia, distancia*0.50))


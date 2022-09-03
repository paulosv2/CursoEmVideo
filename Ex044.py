preco = float(input('Insíra o valor do produto: '))

print('*'*50)
print('*'*50)
print('*'*50)

condicaoPagamento = input('Insíra a forma de pagamento:\nD para dinheiro.\nC para cheque.\nP para cartão de crédito.').upper()

if condicaoPagamento == 'D' or condicaoPagamento == 'C':
    print('O valor para pagamento à vista será: R${:.2f}.'.format(preco*0.9))
else:
    print('*' * 50)
    print('*' * 50)
    print('*' * 50)
    condicaoCartao = input('O pagamento será realizado:\nV - À vista.\nP - Parcelado.').upper()

    if condicaoCartao == 'V':
        print('Para pagamento à vista com o cartão de crédito o valor será de R${:.2f}.'.format(preco*0.95))
    else:
        parcelas = int(input('Insíra o número de parcelas: '))

        if parcelas <= 2:
            print('O valor de cada uma das {} parcelas será de R${:.2f}. O valor total será de {:.2f}.'.format(parcelas, preco/parcelas, preco))
        else:
            print('O valor de cada uma das {} parcelas será de R${:.2f}. O valor total será de {:.2f}.'.format(parcelas, preco*1.2/parcelas, preco*1.2))

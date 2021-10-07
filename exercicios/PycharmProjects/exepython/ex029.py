velo = int(input('Quantos km/h estava o carro? '))
if velo > 80:
    multa = (velo - 80) * 7
    print('Voçe foi multado por excesso de velocidade \nSua multa foi de {}reais'.format(multa))
else:
    print('O condutor nao cometeu infraçoes')


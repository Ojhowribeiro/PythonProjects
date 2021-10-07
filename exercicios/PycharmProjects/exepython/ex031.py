distan = float(input('Qual distancia da viagem em km? '))
pas = distan * 0.50 if distan <= 200 else distan * 0.45
'''if distan <= 200:
    pas = distan * 0.50
else:
    pas = distan * 0.45'''
print('Sua viagem de {}KM vai custar um total de {} reais'.format(distan, pas))

prec = float (input('qual o valor do produto: '))
desc = float (input('qual o valor do desconto: '))
novp = prec - (prec * desc /100)
print('o valor do produto com {}% de desconto fica {} reais'.format(desc, novp))
dias = int(input('quantos dias o carro foi usado? '))
km = float(input('quantos km foram rodados? '))

cust = float((dias * 60) + (km * 0.15))

print('o total a pagar é {:.2f}'.format(cust))
r1 = float(input('Primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É um triangulo:')
    if r1 == r2 == r3:
        print('Equilatero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isosceles!')
else:
    print('Nao é um triangulo')
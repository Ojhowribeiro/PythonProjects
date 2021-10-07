import math

altura = float(input('Qual seu altura em Metros: '))
peso = float(input('Qual o seu peso KG: '))
imc = float(peso / (altura**2))

if imc < 18.5:
    s = 'Abaixo do Peso'
elif 18.5 <= imc < 25:
    s = 'Peso Ideal'
elif 25 <= imc < 30:
    s = 'Sobrepeso'
elif 30 <= imc < 40:
    s = 'Obsidade'
elif imc > 40:
    s = 'Obesidade Morbida'
else:
    print('Valor digitado esta incorreto, tente novamente!!')

print('Seu IMC é {:.1f} e seu status é: {}'.format(imc, s))

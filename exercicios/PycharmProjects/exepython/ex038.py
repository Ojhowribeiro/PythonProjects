num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 > num2:
    print('O numero {} è maior que {}'.format(num1, num2))
elif num2 > num1:
    print('O numero {} é maior que {}'.format(num2, num1))
elif num1 == num2:
    print('Os dois numeros sao iguais!!')

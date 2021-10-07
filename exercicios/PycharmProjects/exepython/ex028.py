from random import randint
from time import sleep

num = randint(0, 5)

print('-' * 25)
num2 = int((input('Digite um numero de 0 a 5 e teste sua sorte!: ')))
print('PROCESSANDO...')
sleep(2)
if num2 == num:
    print('voce acertou!!')
else:
    print('voce errou!!, try again')
print('O numero sorteado foi {}'.format(num))
print('-' * 25)

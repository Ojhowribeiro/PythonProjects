soma = 0
cont = 0

for c in range(1,7):
    num = int(input('digite um numero pela {}°vez:'.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voce digitou {} números PARES, A soma dos números é {}'.format(cont, soma))

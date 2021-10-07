salar = float(input('Qual o seu salario? '))

if salar >= 1250:
    aumen = 10
    salar = salar + (salar * 0.10)
else:
    aumen = 15
    salar = salar + (salar * 0.15)
print('Seu salario com o aumento de {}% agora fica {} reais'.format(aumen, salar))


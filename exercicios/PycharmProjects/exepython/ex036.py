casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('A prestacao sera de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo pede ser concedido!!')
else:
    print('Emprestimo negado!!')


'''valor_casa = int(input('Qual o valor da casa? '))
salario = float(input('qual o salario? '))
anos_pagar = int(input('Quantos anos vai pagar a casa? '))
prestacao = float((valor_casa * 12) / anos_pagar)
salario_30 = (salario*0.30)
if prestacao <= salario_30:
    emprestimo = 'Aprovado'
else:
    emprestimo = 'Reprovado'
print('Seu emprestimo foi {} com uma prestacao de {} por mes'.format(emprestimo, prestacao))'''

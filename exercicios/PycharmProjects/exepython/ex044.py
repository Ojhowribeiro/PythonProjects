preco_compras = float(input('Preço das compras: '))

print('''----Forma de Pagamento----
[1] á vista dinheiro/pix
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual sua opção? '))

if opcao == 1:
      s = preco_compras - (preco_compras * 0.10)
elif opcao == 2:
      s = preco_compras - (preco_compras * 0.05)
elif opcao == 3:
      s = preco_compras
      parcela = s / 2
      print('Sua compra sera parcelada em 2x de R${}'.format(parcela))
elif opcao == 4:
      s = preco_compras + (preco_compras * 0.20)
      totalpar = int(input('Quantas parcelas? '))
      parcela = s / totalpar
      print('Sua compra sera parcelada em {}x de R${:.2f} com juros'.format(totalpar,parcela ))
else:
      s = preco_compras
      print('Opção invalida!!!')

print('Sua compra de R${} vai custar {} no final'.format(preco_compras, s))

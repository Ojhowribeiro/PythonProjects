from datetime import date
ano_atual = date.today().year
nome = str(input('Qual o seu nome? '))
ano_nasceu = int(input('Qual ano voçe nasceu {}?'.format(nome)))
idade = ano_atual - ano_nasceu

if idade <= 9:
    s = 'Mirim'
elif idade > 9 and idade <= 14:
    s = 'Infantil'
elif idade > 14 and idade <= 19:
    s = 'Junior'
elif idade > 19 and idade <= 25:
    s = 'Senior'
elif idade > 25:
    s = 'Master'
else:
    s = 'ERRO, Digite novamente!!!'
print('{} voçe tem {} anos e sua categoria é {}'.format(nome, idade, s))


from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
nome = str(input('Qual seu nome? '))
sexo = input('Voçe é HOMEM ou MULHER?').upper()
print('{} nasceu em {}, tem {} anos em {}'.format(nome, nasc, idade, atual))

if sexo == 'HOMEM':
    if idade == 18:
        print('Voçe tem que se alistar esse ano!!')
    elif idade < 18:
        s = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(s))
        ano = atual + s
        print('Seu alistamento sera em {}'.format(ano))
    elif idade > 18:
        s = idade - 18
        print('Voce ja deveria ter se alistado há {} ano(s)'.format(s))
        ano = atual - s
        print('Seu alistamento foi em {}'.format(ano))
else:
    print('{} nao precisa se alistar. Voce é uma mulher'.format(nome))

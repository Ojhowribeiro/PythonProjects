somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('===== {}° ====='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = nome
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho te {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))
nome_aluno = str(input('Nome do aluno: '))
nota_1 = float(input('Qual foi sua primeira nota? '))
nota_2 = float(input("Qual foi sua segunda nota? "))
media = float((nota_1 + nota_2) / 2)
if media < 5.0:
    status = 'REPROVADO'
elif media >= 5.0 and media <= 6.9:
    status = 'RECUPERAÇÂO'
elif media >= 7.0:
    status = 'APROVADO'
else:
    print('ERRO NO SISTEMA, DIGITE NOVAMENTE')
print('O aluno(a) {} está {}, sua media foi {:.1f}'.format(nome_aluno, status, media))

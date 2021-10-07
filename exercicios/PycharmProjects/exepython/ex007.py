nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = float(nota1+nota2)/2

print('A primeira nota do aluno é: {}\nE a segunda nota é: {}\nA media desse aluno é: {:.1f}'.format(nota1, nota2, media))

if media < 7.0:
    print('Aluno reprovado!')
else:
    print('Aluno aprovado!')

'''n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = float (n1 + n2) /2
print('primeira nota: {}\nsegunda nota: {}\nmedia: {:.2f}'.format(n1, n2, med))'''

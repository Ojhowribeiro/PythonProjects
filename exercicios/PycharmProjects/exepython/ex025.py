'''nome = str(input('Qual é seu nome completo?')).strip().upper()
s = 'SILVA' in nome
print(s)'''

nome = str(input('Qual é seu nome completo?')).strip()
print('Seu nome tem silva? {}'.format('silva' in nome.upper()))

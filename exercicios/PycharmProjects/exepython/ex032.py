'''ano = int(input('Digite um ano para ver se ele é bissesto: '))
anobis = int(ano / 4)
if anobis % 2:
    print('O ano nao é bissesto!!')
else:
    print('O ano é bissesto!!')'''

from datetime import date

ano = int(input('Digite um ano para ver se ele é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O amo {} NAO é BISSEXTO'.format(ano))

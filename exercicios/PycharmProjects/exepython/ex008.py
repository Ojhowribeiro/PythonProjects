medida = float(input('Qual o valor em metros: '))
cm = float(medida*100)
mm = float(medida*1000)
km = float(medida/1000)

print('{} metros: \n{:.3f} cm \n{:.3f} mm\n{:.3f} km'.format(medida, cm, mm, km))

'''medida = float(input('qual a distancia em metros:'))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
print('{} metros igual:\ncm: {}\nmm: {}\nkm: {}'.format(medida, cm, mm, km))'''
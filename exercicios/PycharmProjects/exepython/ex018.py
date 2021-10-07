import math
an = float(input('Qual o angulo? '))
sen = math.sin(math.radians(an))
print('O angulo de {} tem o SENO de {:.2f}'.format(an, sen))
cos = math.cos(math.radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('O anggulo de {} tem a TANGENTE de {:.2f}'.format(an, tan))

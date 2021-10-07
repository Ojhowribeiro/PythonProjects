num = int(input('Digite um número para ver sua tabuada: '))

print('-/' *15)
for c in range(1, 11):
    print('{} X {} = {}'.format(num, c, num*c))
print('-/' *15)

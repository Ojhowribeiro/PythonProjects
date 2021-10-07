


nome = str(input('Qual o seu nome:')).strip()
print('seu nome com todas as letras maiusculas: {}'.format(nome.upper()))
print('seu nome com todas as letras minusculas: {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' '))) #tiras os espacos entre as palavras
#print('o primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split() #separa a frase entre os espaços
print('seu primeiro nome è {} e tem {} letras'.format(separa[0], len(separa[0])))




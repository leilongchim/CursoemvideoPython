print('Lê o nome de uma pessoa, e mostra o primeiro e o ultimo nome separadamente')
nome = input('Escreva seu nome completo: ')
nome = nome.title()
sep = nome.split()
print('Primeiro nome: {}'.format(sep[0]))
sep.reverse()
print('Último nome? {}'.format(sep[0]))
print(nome)

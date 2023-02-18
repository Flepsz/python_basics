print('Pode digitar seu nome com letras maiúsculas, minúsculas ou mistas.')
nome = input('Informe o nome: ')
tam = len(nome)

for x in range(tam):
    print(nome[:tam-x].upper())

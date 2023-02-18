print('Pode digitar seu nome com letras maiúsculas, minúsculas ou mistas.')
nome = input('Digite seu nome: ').upper()
lista = list(nome)
for x in lista[::-1]:
    print(x)

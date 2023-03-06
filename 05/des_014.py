homem_velho = ""
velho = 0
menor20 = 0
total = 0
media = 0

for i in range(1, 5):
    print("---------- {}ª Pessoa ----------".format(i))
    nome = input("Nome: ").title()
    idade = int(input("Idade: "))
    sexo = input("Sexo(M/F): ").upper()

    total += idade
    media = total / i

    if idade > velho and sexo == "M":
        velho = idade
        homem_velho = nome

    if idade < 20 and sexo == "F":
        menor20 += 1

print("-" * 35)
print("Média de idade: {:.2f}".format(media))
print("Nome do homem mais velho: {}".format(homem_velho))
print("Mulhere(s) abaixo de 20 anos = {}".format(menor20))
print("-" * 35)

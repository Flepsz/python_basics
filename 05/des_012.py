from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

print("-" * 45)

for i in range(1, 8):
    ano = int(input("Ano de nascimento {}ª da pessoa: ".format(i)))
    if ano_atual - ano >= 18:
        maior += 1
    elif ano_atual - ano < 18:
        menor += 1

print("Total maiores= \033[34m{}\033[m \nTotal menores= \33[31m{}\033[m".format(maior, menor))

print("-" * 45)

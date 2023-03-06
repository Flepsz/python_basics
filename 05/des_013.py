maior = 0
menor = 0

print("-" * 45)


for i in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("Maior peso= \033[34m{}Kg\033[m \nMenor peso= \33[31m{}Kg\033[m".format(maior, menor))

print("-" * 45)

print("-" * 30)

soma = 0

for i in range(1, 7):
    n = int(input("Digite o {}º valor: ".format(i)))
    if n % 2 == 0:
        soma += n

print("Total: {}".format(soma))

print("-" * 30)

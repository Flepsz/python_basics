lis = []
pares = []
impares = []

print('-' * 30)

while True:
    val = int(input("Digite um valor: "))
    lis.append(val)
    if val % 2 == 0:
        pares.append(val)
    if val % 3 == 0:
        impares.append(val)
    op = input("Deseja continuar? [S/N]: ").upper()
    if op in 'N':
        break

print("Lista:  {}".format(lis))
print("Pares:  {}".format(pares))
print("Ímpares:  {}".format(impares))

print('-' * 30)

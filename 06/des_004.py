lis = list()

print('-' * 30)

while True:
    val = int(input("Digite um valor: "))
    lis.append(val)
    lis.sort()
    op = input("Deseja continuar? [S/N]: ").upper()
    if op in 'N':
        break

print("Qde de valores: {}".format(len(lis)))
print("Valores decrescentes: {}".format(lis[::-1]))

if 5 in lis:
    print("5 está na lista")

print('-' * 30)

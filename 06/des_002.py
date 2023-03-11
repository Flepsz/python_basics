lis = []

while True:
    val = int(input("Digite um valor: "))
    if val not in lis:
        lis.append(val)
    lis.sort()
    print(lis)
    op = input("Deseja continuar? [S/N]: ").upper()
    if op in 'N':
        break


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
impares = 0
soma3 = 0

print('-' * 35)
for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = int(input("Digite um valor para [{}][{}]: ".format(a, b)))

print('-' * 35)
for a in range(0, 3):
    for b in range(0, 3):
        print('[{:^5}]'.format(matriz[a][b]), end='')
        if matriz[a][b] % 2 == 0:
            pares += matriz[a][b]
        else:
            impares += matriz[a][b]
    print()

print("Total Pares: {}".format(pares))
print("Total Ímpares: {}".format(impares))

for a in range(0, 3):
    soma3 += matriz[a][2]
print('Soma da 3ª coluna: {}'.format(soma3))

print('Maior valor da 2ª linha: {}'.format(max(matriz[1])))

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print('-' * 30)
for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = int(input("Digite um valor para [{}][{}]: ".format(a, b)))

print('-' * 30)
print(matriz[0])
print(matriz[1])
print(matriz[2])

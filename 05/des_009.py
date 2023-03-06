print('-' * 30)
prim = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for i in range(prim, 20, razao):
    print('{}'.format(i), end=' ')

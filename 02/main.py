n = int(input('Digite um numero: '))

for y in range(0, 11):
    print('{} X {} = {}'.format(n, y, n*y))
    y += 1
print('='*20)

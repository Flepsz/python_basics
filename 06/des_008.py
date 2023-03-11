lis = [[], []]

print('-' * 30)
for i in range(0, 7):
    n = int(input('Digite o {}º valor: '.format(i + 1)))
    if n % 2 == 0:
        lis[0].append(n)
    else:
        lis[1].append(n)

print('-' * 30)
print("Pares: {}".format(lis[0]))
print("Ímpares: {}".format(lis[1]))

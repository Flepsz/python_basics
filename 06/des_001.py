val = []

for i in range(0, 5):
    val.append(int(input('Digite um número na posição {}º: '.format(i))))

print(val)
print('Maior: {} na posição {}'.format(max(val), val.index(max(val))))
print('Menor: {} na posição {}'.format(min(val), val.index(min(val))))


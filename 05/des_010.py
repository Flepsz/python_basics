print('-' * 30)

div = 0
color = {
    'y': '\033[33m',
    'c': '\033[m'
}

n = int(input("Digite um número: "))

for i in range(1, n + 1):
    if n % i == 0:
        print("\033[34m", end="")
        div += 1
    else:
        print("\033[31m", end="")
    print("{} ".format(i), end="")

if div == 2:
    print("\n{}{}O número {} é primo{}.".format(color['c'], color['y'], n, color['c']))
else:
    print("\n{}{}O número {} não é primo{}.".format(color['c'], color['y'], n, color['c']))

print('-' * 30)

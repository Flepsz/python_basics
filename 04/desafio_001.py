def decBin():
    dec = int(input('Digite um número decimal: '))
    decint = dec
    lis = ''

    while decint >= 1:
        lis += str(decint % 2)
        decint //= 2

    f = lis[::-1]
    print('Seu em binário é {}'.format(f))
    print('\n')

def decHex():
    dec = int(input('Digite um número decimal: '))
    lis = ''
    vet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    while dec >= 1:
        decx = dec % 16
        lis += vet[decx]
        dec //= 16

    print('Seu número em hexadecimal é {}'.format(lis[::-1]))
    print('\n')

def binDec():
    bin = int(input('Digite um número binário: '))
    a = len(str(bin))
    dec = 0
    i = 0

    while a >= 0:
        resto = bin % 10
        dec = dec + (resto * (2 ** i))
        a = a - 1
        i = i + 1
        bin = bin // 10

    print('Seu número em decimal é {}'.format(dec))
    print('\n')

def binHex():
    bin = int(input('Digite um número binário: '))
    a = len(str(bin))
    dec = 0
    i = 0
    lis = ''
    vet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    while a >= 0:
        resto = bin % 10
        dec = dec + (resto * (2 ** i))
        a = a - 1
        i = i + 1
        bin = bin // 10

        decx = dec % 16
        lis += vet[decx]
        dec //= 16

        print('Seu número em hexadecimal é {}'.format(lis[::-1]))
        print('\n')


while True:
    print('Menu: ')
    print('[0] Sair')
    print('[1] Decimal -> Binário')
    print('[2] Decimal -> Hexadecimal')
    print('[3] Binário -> Decimal')
    print('[4] Binário -> Hexadecimal')
    print('[5] Voltar')

    op = int(input('Escolha uma opção: '))

    if op == 0:
        break

    elif op == 1:
        decBin()
    elif op == 2:
        decHex()
    elif op == 3:
        binDec()
    elif op == 4:
        binHex()
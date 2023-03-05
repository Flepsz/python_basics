def bina():
    decint = num
    lis = ''

    while decint >= 1:
        lis += str(decint % 2)
        decint //= 2

    f = lis[::-1]
    print('Binário: {}{}{}'.format('\033[7;93m', f, '\33[m'))
    print('\n')


def octa():
    octal = 0
    ctr = 0
    temp = num

    while temp > 0:
        octal += ((temp % 8) * (10 ** ctr))
        temp = int(temp / 8)
        ctr += 1
    print('Octal: {}{}{}'.format('\033[7;37;94m', octal, '\33[m'))


def hexa():
    dec = num
    lis = ''
    vet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    while dec >= 1:
        decx = dec % 16
        lis += vet[decx]
        dec //= 16

    print('Hexadecimal: {}{}{}'.format('\033[7;95m', lis[::-1], '\33[m'))
    print('\n')


while True:
    num = int(input('Digite um número: '))
    print('Escolha uma das bases: ')
    print('[1] Binário')
    print('[2] Octal')
    print('[3] Hexadecimal')
    op = int(input('Sua opção: '))

    if op == 1:
        bina()
    elif op == 2:
        octa()
    elif op == 3:
        hexa()
    elif op >= 4:
        print('{}Opção inválida{}.'.format('\33[1;31m', '\33[m'))
        break

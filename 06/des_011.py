from random import randint

lista = []
jogos = []
total = 1

print('-' * 35)
print('            MEGA SENA')
print('-' * 35)
n = int(input('Quantos jogos deseja? '))

while total <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-------- Sorteando {} jogos --------'.format(n))
for i, l in enumerate(jogos):
    print("Jogo {}: {}".format(i + 1, l))
print('-' * 35)

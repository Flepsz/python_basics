from random import randint
from operator import itemgetter
ordem = {}
jogadores = {
    "Jogador1": randint(1, 6),
    "Jogador2": randint(1, 6),
    "Jogador3": randint(1, 6),
    "Jogador4": randint(1, 6)
}

print('--' * 20)

for pos, val in jogadores.items():
    print("O {} sorteou {}.".format(pos, val))

ordem = sorted(jogadores.items(), key=itemgetter(1))

print('--' * 20)

v = 1
for pos, val in ordem[::-1]:
    print("O {}º lugar: {} com {}.".format(v, pos, val))
    v += 1

print('--' * 20)

color = {
    'r': '\33[1;31m',
    'c': '\33[m'
    # color['c']
    # color['r']
}

print('--' * 25)

avaliador = {
    'aluno': input('Aluno: '),
}
avaliador['nota'] = float(input('Nota do(a) {}: '.format(avaliador['aluno'])))

if avaliador['nota'] <= 3.9:
    avaliador['situação'] = 'Reprovado'
elif avaliador['nota'] <= 6.9:
    avaliador['situação'] = 'Recuperação'
else:
    avaliador['situação'] = 'Aprovado'

for pos, val in avaliador.items():
    print("{}{}{} é igual à {}{}{}".format(color['r'], pos, color['c'], color['r'], val, color['c']))

print('--' * 25)

cores = {
    'Reprovado': '\33[1;31m',
    'Aprovado': '\33[1;34m',
    'Limpa': '\33[m'
}
media = float(input('Digite a média: '))
freq = float(input('Digite a frequência: '))

if media >= 50 and freq >= 75:
    r = 'Aprovado'
else:
    r = 'Reprovado'

print('Média: {}{}{}'.format(cores[r], media, cores["Limpa"]))
print('Freq: {}{}{}'.format(cores[r], freq, cores['Limpa']))

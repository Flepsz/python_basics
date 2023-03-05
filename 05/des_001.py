cores = {
    'Negado': '\33[1;30;41m',
    'Liberado': '\33[1;30;42m',
    'Limpa': '\33[m'
}

vlcasa = float(input('Valor da casa: R$'))
sal = float(input('Salário: R$'))
anos = float(input('Qte anos: '))
nparcela = anos * 12
vlparcela = vlcasa / nparcela

print('-' * 30)
print('Valor da casa: R$ {:.2f}'.format(vlcasa))
print('Salário: R$ {:.2f}'.format(sal))
print('Prestação: R$ {:.2f}'.format(vlparcela))

if vlparcela <= sal * 0.30:
    r = 'Liberado'
    print('{}{}{}'.format(cores[r], r, cores["Limpa"]))
else:
    r = 'Negado'
    print('{}{}{}'.format(cores[r], r, cores["Limpa"]))
    print('Máximo: {}R$ {:.2f}{}'.format('\033[1;30;41m', (sal * 0.30), '\33[m'))


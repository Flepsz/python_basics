# Tirar carteira de Motorista
# Parecido coom o desafio 03, mas com mais detalhes.
from datetime import date

ano = date.today().year
mes = date.today().month
dia = date.today().day

dianas = int(input('Digite seu dia de nascimento: '))
mesnas = int(input('Digite seu mês de nascimento: '))
anonas = int(input('Digite seu ano de nascimento: '))
idade = ano - anonas
print('-' * 30)
print('Ano de nascimento: {}'.format(anonas))
print('Idade: {} anos'.format(ano - anonas))

if idade < 18:
    print('Falta(m) {} ano(s) para tirar sua carteira de motorista'.format(18 - idade))

elif idade == 18:
    if mesnas <= mes and dianas <= dia:
        print('Ja pode tirar sua carteira de motorista')
    if mesnas == mes and dianas > dia:
        print('Falta(m) {} dia(s) para tirar sua carteira de motorista'.format(dianas - dia))
    else:
        print('Falta(m) {} mes(es) para tirar sua carteira de motorista'.format(mesnas - mes))

elif idade > 18:
    print('Ja pode tirar sua carteira de motorista')
print('-' * 30)

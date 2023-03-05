from datetime import date

ano = date.today().year
mes = date.today().month
dia = date.today().day

dianas = int(input('Digite seu dia de nascimento: '))
mesnas = int(input('Digite seu mês de nascimento: '))
anonas = int(input('Digite seu ano de nascimento: '))
idade = ano - anonas
print('-' * 30)
print('Idade: {} anos'.format(ano - anonas))

if idade < 18:
    print('Falta(m) {} ano(s) para se alistar'.format(18 - idade))

elif idade == 18:
    print('Hora de se alistar!')

elif idade > 18:
    print('Passou do tempo faz(em) {} ano(s)'.format(idade - 18))
print('-' * 30)

print('Transforme decimal para binário!')
dec = int(input('Digite um número decimal: '))
decint = dec
quo = 1
lis = ''

while quo >= 1:
    resto = dec % 2
    lis += str(resto)
    quo = dec // 2
    dec = quo

f = lis[::-1]
print('Seu número em decimal é {} e em binário é {}'.format(decint, f))

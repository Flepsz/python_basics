import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa é {}'.format(math.hypot(co,ca)))
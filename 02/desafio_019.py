from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, sen))
cos = cos(radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cos))
tan = tan(radians(angulo))
print('O ângulo de {} tem o tangente de {:.2f}'.format(angulo, tan))

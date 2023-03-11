expressao = str(input('Expressão: '))
lis = []

for simbolo in expressao:
    if simbolo == '(':
        lis.append('(')
    elif simbolo == ')':
        if len(lis) > 0:
            lis.pop()
        else:
            lis.append(')')
            break

if len(lis) == 0:
    print('Expressão válida...')
else:
    print("Expressão inválida...")

cadastro = []
todos = []
maior = 0
menor = 0

while True:
    cadastro.append(input("Nome: ").title())
    cadastro.append(float(input("Peso: ")))
    if len(todos) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    todos.append(cadastro[:])
    cadastro.clear()

    op = input("Deseja continuar? [S/N]: ").upper()
    if op in 'N':
        break


print("Total de cadastros: {}".format(len(todos)))
for p in todos:
    if p[1] == maior:
        print("Maior peso: {} com {}kg".format(p[0], maior))
for p in todos:
    if p[1] == menor:
        print("Menor peso: {} com {}kg".format(p[0], menor))

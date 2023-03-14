import inquirer

cadastro = []
clientes = []
novo_usuario = []


def menu():
    while True:
        print('[0] - Sair\n'
              '[1] - Cadastrar\n'
              '[2] - Entrar\n')
        op = int(input('Escolha a opção: '))
        if op == 0:
            break

        elif op == 1:
            nome = input('Nome: ')
            cadastro.append(nome)
            email = input('Email: ')
            cadastro.append(email)
            questions = [
                inquirer.List('modes',
                              message="Choose the difficulty level",
                              choices=['Basic', 'Medium', 'Premium'],
                              ),
            ]
            answers = inquirer.prompt(questions)
            planos = answers['modes']
            cadastro.append(planos)
            clientes.append(cadastro[:])
            cadastro.clear()
            print(clientes)

        elif op == 2:
            cliente = input('Nome: ')
            for i in range(len(clientes)):
                if cliente == cliente[i][0]:
                    novo_usuario.append(clientes[i][0])
                    novo_usuario.append(clientes[i][1])
                    novo_usuario.append(clientes[i][2])
            break

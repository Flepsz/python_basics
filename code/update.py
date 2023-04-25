from prettytable import PrettyTable
from connect import conexao


cursor = conexao.cursor()


def update_user():
    email = input("Digite o e-mail com permissão para atualizar o usuário: ")
    sql = f"SELECT tipo FROM usuarios WHERE email = {email}"
    cursor.execute(sql)
    result = cursor.fetchone()

    if result is None:
        print("Usuário não encontrado")
    elif result[0] != "Admin":
        print("Acesso negado. Você não tem permissão para atualizar esse usuário.")
    else:
        nome = input("Digite o novo nome do usuário: ")
        idade = int(input("Digite a nova idade do usuário: "))
        plano = input("Digite o novo plano do usuário (Basic, Medium ou Premium): ").title()
        sql = f"UPDATE usuarios SET usuario = {nome}, idade = {idade}, plano = {plano} WHERE email = {email}"
        cursor.execute(sql)
        conexao.commit()

        print("Usuário atualizado com sucesso")


def update_film():
    email = input("Digite o e-mail do usuário com permissão para atualizar filmes: ")
    sql = f"SELECT tipo FROM usuarios WHERE email = {email}"
    cursor.execute(sql)
    result = cursor.fetchone()

    if result is None:
        print("Usuário não encontrado")
    elif result[0] != "Admin":
        print("Acesso negado. Você não tem permissão para atualizar filmes.")
    else:
        id_filme = input("Digite o id do filme a ser atualizado: ")
        filme = input("Digite o novo título do filme: ")
        plano = input("Digite o novo plano do usuário (Basic, Medium ou Premium): ").title()
        desc = input("Digite uma nova descrição para o filme: ")
        sql = f"UPDATE filmes SET filme = {filme}, plano = {plano}, desc = {desc} WHERE id_filme = {id_filme}"
        cursor.execute(sql)
        conexao.commit()

        print("Filme atualizado com sucesso")


def up_usuario(idUser, usuario, email, plano, tipo, idade):
    try:
        sql = f"""UPDATE usuarios SET usuario='{usuario}', email = '{email}', plano = '{plano}', 
        tipo = '{tipo}', idade = '{idade}' WHERE idUsuario = '{idUser}';"""
        cursor.execute(sql)
        conexao.commit()
        print("Atualização de dados bem sucedida...")
    except:
        print("Erro ao inserir os dados...")


def up_filme():
    try:
        sql = 'SELECT * from filmes'
        cursor.execute(sql)
        linhas = cursor.fetchall()
        tabela = PrettyTable()
        tabela.field_names = ["ID", "Filme", "Plano", "Descrição", "Classificação"]

        for linha in linhas:
            tabela.add_row(linha)
        print(tabela)

        id = input('Entre com o ID do filme: ')

        sql = f"""SELECT * FROM filmes WHERE idFilme = '{id}';"""
        cursor.execute(sql)
        linhas = cursor.fetchall()
        tabela = PrettyTable()
        tabela.field_names = ["ID", "Filme", "Plano", "Descrição", "Classificação"]

        for linha in linhas:
            tabela.add_row(linha)
        print(tabela)

        filme = input("Filme: ")
        plano = input("Plano: ")
        descricao = input("Descrição: ")
        classs = input("Classificação: ")

        sql = f"""UPDATE filmes SET filme='{filme}', plano = '{plano}', descricao = '{descricao}', 
        class = '{classs}' WHERE idFilme = '{id}';"""
        cursor.execute(sql)
        conexao.commit()
    except:
        print("Erro ao inserir os dados do filme...")
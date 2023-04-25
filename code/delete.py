from prettytable import PrettyTable

from connect import conexao

cursor = conexao.cursor()


def excluir_user():
    email = input("Digite o e-mail com permissão para excluir o usuário: ")
    sql = "SELECT tipo FROM usuarios WHERE email = %s"
    val = (email,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        print("Usuário não encontrado")
    elif result[0] != "Admin":
        print("Acesso negado. Você não tem permissão para excluir esse usuário.")
    else:
        id_usr = int(input("Digite o id do usuário a ser excluído: "))
        sql = f"DELETE FROM filmes WHERE idUsuario = {id_usr}"
        cursor.execute(sql)
        conexao.commit()

        print("Usuário excluído com sucesso")


def excluir_film():
    email = input("Digite o e-mail com permissão para excluir o filme: ")
    sql = "SELECT tipo FROM usuarios WHERE email = %s"
    val = (email,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        print("Usuário não encontrado")
    elif result[0] != "Admin":
        print("Acesso negado. Você não tem permissão para excluir filmes.")
    else:
        id_filme = int(input("Digite o ID do filme a ser excluído: "))
        sql = f"DELETE FROM filmes WHERE idFilme = {id_filme}"
        cursor.execute(sql)
        conexao.commit()

        if cursor.rowcount == 0:
            print("Filme não encontrado")
        else:
            print("Filme excluído com sucesso")


def del_usuario(idUser):
    try:
        sql = f"""DELETE FROM usuarios WHERE idUsuario = '{idUser}';"""
        cursor.execute(sql)
        conexao.commit()
        print("Sucesso ao apagar os dados...")
    except:
        print("Erro ao apagar os dados...")


def del_filme(id):
    try:
        sql = 'SELECT * from filmes'
        cursor.execute(sql)
        cursor.fetchall()

        sql = f"""SELECT * FROM filmes WHERE idFilme = '{id}';"""
        cursor.execute(sql)
        cursor.fetchall()

        resp = input(f'Deseja realmente apagar? [S/N]').strip().upper()
        if resp == 'S':
            sql = f"""DELETE FROM filmes WHERE idFilme = '{id}';"""
            cursor.execute(sql)
            conexao.commit()
    except:
        print("Erro ao apagar os dados...")
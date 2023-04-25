import getpass
from mysql.connector.errors import Error
from prettytable import PrettyTable

from connect import conexao

cursor = conexao.cursor()


def login():
    try:
        email = input("Digite seu e-mail: ")
        senha = getpass.getpass("Digite sua senha: ")

        sql = f"SELECT * FROM usuarios WHERE email = {email} AND senha = {senha}"
        cursor.execute(sql)
        result = cursor.fetchone()

        if result:
            print("Login efetuado com sucesso")
        else:
            print("E-mail ou senha inválidos")

    except Error as e:
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


def ler_usuarios():
    email = input("Digite o e-mail do usuário com permissão para listar: ")
    sql = f"SELECT tipo FROM usuarios WHERE email = {email}"
    cursor.execute(sql)
    tipo_usuario = cursor.fetchone()[0]

    if tipo_usuario == "Admin":
        try:
            sql = 'SELECT * from usuarios'
            cursor.execute(sql)
            result = cursor.fetchall()

            id_width = 4
            nome_width = 20
            email_width = 25
            senha_width = 17
            plano_width = 20
            tipo_width = 18
            idade_width = 10

            header = f"|{'ID':^{id_width}}|{'NOME':^{nome_width}}|{'E-MAIL':^{email_width}}|" \
                     f"{'SENHA':^{senha_width}}|{'PLANO':^{plano_width}}|{'TIPO':^{tipo_width}}|{'IDADE':^{idade_width}}"

            print("-" * len(header))
            print(header)
            print("-" * len(header))

            for usuarios in result:
                usuarios = f"|{usuarios[0]:^{id_width}}|{usuarios[1]:^{nome_width}}|{usuarios[2]:^{email_width}}|" \
                           f"{usuarios[3]:^{senha_width}}|{usuarios[4]:^{plano_width}}|{usuarios[5]:^{tipo_width}}|" \
                           f"{usuarios[6]:^{idade_width}}"
                print(usuarios)
            print("-" * len(header))
            print('\n\n')

        except Error as e:
            print(f'Erro: {e}')

        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    else:
        print("Acesso negado. Você não tem permissão para listar usuários.")


def ler_filmes():
    try:
        sql = 'SELECT * from  filmes'
        cursor.execute(sql)
        linhas = cursor.fetchall()

        id_width = 4
        titulo_width = 40
        plano_width = 17
        descricao_width = 60
        classificacao_width = 18

        header = f"|{'ID':^{id_width}}|{'TÍTULO':^{titulo_width}}|{'PLANO':^{plano_width}}|" \
                 f"{'DESCRIÇÃO':^{descricao_width}}|{'CLASSIFICAÇÃO':^{classificacao_width}}|"

        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for linha in linhas:
            filmes = f"|{linha[0]:^{id_width}}|{linha[1]:^{titulo_width}}|{linha[2]:^{plano_width}}|" \
                     f"{linha[3]:^{descricao_width}}|{linha[4]:^{classificacao_width}}|"
            print(filmes)
        print("-" * len(header))
        print('\n\n')

    except Error as e:
        print(f'Erro: {e}')

    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()


def listar_usuarios():
    sql = 'SELECT * from usuarios'
    cursor.execute(sql)
    return cursor.fetchall()


def procurar_usuario(idUser):
    sql = f"SELECT * from usuarios WHERE idUsuario = '{idUser}'"
    cursor.execute(sql)
    return cursor.fetchall()


def listar_filmes():
    sql = 'SELECT * from filmes'
    cursor.execute(sql)
    return cursor.fetchall()

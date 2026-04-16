from database.conexao import Conexao
import hashlib

class Usuarios():
    def cadastrar_usuario(nome, usuario, senha):
        try:
            conexao, cursor = Conexao.conectar()

            cursor.execute("""INSERT INTO usuarios(nome, usuario, senha)VALUES(%s, %s, %s)""", [nome, usuario, senha])
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro:
            print(erro)
            return False




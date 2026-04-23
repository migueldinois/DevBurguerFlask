from database.conexao import Conexao

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
        
    @staticmethod
    def verificar_usuario(usuario:str, senha:str) -> dict:
        try:
            conexao, cursor = Conexao.conectar()

            cursor.execute("""SELECT * from usuarios where usuario = %s AND senha = %s""", [usuario, senha])
            usuario = cursor.fetchone()
            conexao.commit()
            conexao.close()
            return usuario


        except Exception as erro:
            print(erro)
            return False





from database.conexao import Conexao

class Produtos():
    def recuperar_produtos():
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT produto, descricao, preco, destaque, foto, disponibilidade')
        produtos = cursor.fetchall()
        return produtos
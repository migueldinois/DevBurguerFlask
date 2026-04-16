from database.conexao import Conexao

class Produtos():
    def recuperar_produtos():
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM produtos')
        produtos = cursor.fetchall()
        return produtos
    
    def detalhes_produto(codigo):
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM produtos WHERE codigo = %s', 
                       [codigo])
        produtos = cursor.fetchone()
        return produtos
    
    def recuperar_destaques():
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM produtos WHERE destaque = 1')
        destaques = cursor.fetchall()
        return destaques
    
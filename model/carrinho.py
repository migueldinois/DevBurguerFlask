from database.conexao import Conexao


class Carrinho():
    def recuperar_carrinho( usuario:str )-> list:

        conexao, cursor = Conexao.conectar()

        cursor.execute("""
            SELECT carrinhos.cod_carrinho,
                usuarios.usuario,
                carrinhos.data,
                carrinhos.finalizado,
                produtos.produto,
                itens_carrinho.quantidade,
                produtos.preco,
                produtos.foto
            FROM carrinhos
            INNER JOIN usuarios ON carrinhos.usuario = usuarios.usuario
            INNER JOIN itens_carrinho ON carrinhos.cod_carrinho = itens_carrinho.cod_carrinho
            INNER JOIN produtos ON produtos.codigo = itens_carrinho.cod_produto
        """)


        produto = cursor.fetchall()

        conexao.close()

        return produto
    
    def adicionar_item_carrinho(cod_produto, cod_carrinho, quantidade):
        try:
            conexao, cursor = Conexao.conectar()

            cursor.execute("""

                INSERT INTO itens_carrinho (cod_produto, cod_carrinho, quantidade) 
                VALUES (%s, %s, %s);
                """, [cod_produto, cod_carrinho, quantidade])
            conexao.commit()
            conexao.close()
            return True        
        except Exception as erro:
            print(erro)
            return False
        
    def verificar_carrinho_existente(cod_carrinho:int):
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT cod_carrinho, usuario, finalizado disponibilidade FROM carrinhos')
        carrinho = cursor.fetchone()
        return carrinho

        
    def criar_carrinho_novo(usuario:str, finalizado:bool):
        
        try:
            conexao,cursor = Conexao.conectar()
            cursor.execute("""
                INSERT INTO carrinhos(usuario,finalizado)
                        VALUES(%s,%s)
            """, [usuario, finalizado])
            conexao.commit()
            conexao.close()
            return True
        
        except Exception as erro:
            print(erro)
            return False
        
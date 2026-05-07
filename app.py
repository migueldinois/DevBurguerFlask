from flask import Flask, render_template, request, redirect, session, jsonify
from model.produtos import Produtos
from model.usuarios import Usuarios
from model.carrinho import Carrinho


app = Flask(__name__)
app.secret_key = '777'

@app.route('/')
def pagina_principal():
    produtos = Produtos.recuperar_produtos()
    destaques = Produtos.recuperar_destaques()
    return render_template("index.html", produtos = produtos, destaques = destaques)

@app.route('/detalhes_produto/<codigo>')
def layout(codigo):
    produto = Produtos.detalhes_produto(codigo)
    return render_template("detalhes.html", produto = produto)

@app.route('/login')
def login_pagina():
    if "usuario" in session:
        return redirect("/")
    else:
        return render_template("login.html")

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    input_nome = request.form.get("nome")
    input_email = request.form.get("email")
    input_senha = request.form.get("senha")
    usuario_logado = Usuarios.cadastrar_usuario(input_nome, input_email, input_senha)
    session["usuario_logado"] = usuario_logado
    return redirect("/login")

@app.route('/logar', methods=['POST'])
def logar():
    input_email = request.form.get("email")
    input_senha = request.form.get("senha")

    resposta = Usuarios.verificar_usuario(input_email, input_senha)
    print(resposta)
    if resposta != None:
        session["usuario_logado"] = resposta
        return redirect("/")
    else:
        print("Usuario ou senha incorretos")
        return redirect("/login")
    
@app.route("/api/get/carrinho", methods=["GET"])
def api_get_carrinho():
    if "usuario_logado" in session:
        login = session["usuario_logado"]["usuario"]
        # Pegando o carrinoh e mandando com json
        carrinho = Carrinho.recuperar_carrinho(login)
        return jsonify(carrinho), 200
    else:
        return jsonify({"error": "Usuário não logado"}), 401

@app.route("/api/post/carrinho", methods=["POST"])
def api_adicionar_item_carrinho():
    if "usuario_logado" in session:
        dados = request.get_json()
        cod_produto = dados.get("cod_produto")
        quantidade = dados.get("quantidade")
        
        login = session["usuario_logado"]["usuario"]
        
        cod_carrinho = Carrinho.verificar_carrinho_aberto(login)
        # Se nao tiver codigo carrinho, cria um novo
        if not cod_carrinho:
            cod_carrinho = Carrinho.criar_carrinho_novo(login)
            
        # Aidiconando
        if cod_carrinho and Carrinho.adicionar_item_carrinho(cod_produto, cod_carrinho, quantidade):
            
            return jsonify({"message":"Inserido com sucesso"}), 201
        
        return "Erro ao processar carrinho", 500
    else:
        return redirect("/login")




if __name__ == '__main__':
    app.run(debug=True) 
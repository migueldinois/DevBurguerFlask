from flask import Flask, render_template, request, redirect
from model.produtos import Produtos
from model.usuarios import Usuarios


app = Flask(__name__)

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
    return render_template("login.html")

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    input_nome = request.form.get("nome")
    input_email = request.form.get("email")
    input_senha = request.form.get("senha")
    if Usuarios.cadastrar_usuario(input_nome, input_email, input_senha):
        return redirect("/login")




if __name__ == '__main__':
    app.run(debug=True) 
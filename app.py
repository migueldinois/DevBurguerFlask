from flask import Flask, render_template, request, redirect, session
from model.produtos import Produtos
from model.usuarios import Usuarios


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
    session["usuario"] = input_nome
    return redirect("/login")

@app.route('/logar', methods=['POST'])
def logar():
    input_email = request.form.get("email")
    input_senha = request.form.get("senha")
    

    


if __name__ == '__main__':
    app.run(debug=True) 
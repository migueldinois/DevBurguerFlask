from flask import Flask, render_template
from model.produtos import Produtos

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



if __name__ == '__main__':
    app.run(debug=True) 
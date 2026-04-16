from flask import Flask, render_template
from model.produtos import Produtos

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    produtos = Produtos.recuperar_produtos()
    return render_template("index.html", produtos = produtos)

@app.route('/detalhes_produto/<codigo>')
def layout():
    return render_template("detalhes.html")



if __name__ == '__main__':
    app.run(debug=True) 
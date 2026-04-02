from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template("index.html")

@app.route('/detalhes_produto/<codigo>')
def layout():
    return render_template("detalhes.html")



if __name__ == '__main__':
    app.run(debug=True) 
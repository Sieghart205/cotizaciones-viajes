from flask import Flask,render_template,send_from_directory
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

IMG = os.path.join("img")
app.config["IMG"] = IMG

@app.route("/img/<foto>")
def img(foto):
    return send_from_directory(app.config["IMG"],foto)


CSS = os.path.join("css")
app.config["CSS"] = CSS

@app.route("/css/<nombreArchivo>")
def css(nombreArchivo):
    return send_from_directory(app.config["CSS"],nombreArchivo)

@app.route("/")
def raiz():
    return render_template("index.html")

@app.route("/computador")
def computador():
    return render_template("computador.html")

@app.route("/imprimir")
def imprimir():
    return render_template("imprimir.html")


if __name__ == "__main__":
    app.run(debug=True)
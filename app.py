from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hello_YOU():
    return "<p>Hello, YOU</p>"
@app.route("/chau")
def Goodbye_you():
    return "<p>Goodbye, YOU</p>"
@app.route("/saludar/por-nombre/<string:nombre>")
def sxn(nombre):
    return f"<p>Hola, {nombre}</p>"

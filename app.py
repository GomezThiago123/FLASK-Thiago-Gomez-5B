from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hello_world():
    return "<p>Hello, YOU</p>"
@app.route("/chau")
def Goodbye_you():
    return "<p>Goodbye, YOU</p>"
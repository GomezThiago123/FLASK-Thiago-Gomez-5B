from flask import Flask, render_template, url_for
import sqlite3
def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}

def abrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = dict_factory
    
def cerrarConexion():
    global db
    db.close()
    db = None
        
app = Flask(__name__)

@app.route("/hola")
def hello_world():
    return "<p>Hello, YOU</p>"
@app.route("/chau")
def Goodbye_you():
    return "<p>Goodbye, YOU</p>"

@app.route("/test-db")
def testDB():
    abrirConexion()
    cursor = db.cursor()
    consulta = "SELECT COUNT(*) AS cant FROM usuarios; "
    cursor.execute(consulta)
    res = cursor.fetchone()
    registros = res["cant"]
    cerrarConexion()
    return f"Hay {registros} usuarios"
    
@app.route("/crear-usuario")
def testCrear():
    nombre = "Thiago"
    email = "thiagogomez12300@gmail.com"
    abrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuarios(usuario,email) VALUES (?,?);"
    cursor.execute(consulta, (nombre, email))
    db.commit()
    return f"{nombre} y {email}"


##CON ARGUMENTOS
@app.route("/crear-usuario/<string:nombre>/<string:email>")
def testCrearXArgu(nombre,email):
    abrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuarios(usuario,email) VALUES (?,?);"
    cursor.execute(consulta, (nombre, email))
    db.commit()
    return f"{nombre}"

print(app.url_map)

@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email FROM usuarios WHERE id = ?;",(id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    if res != None:
        usuario = res['usuario']
        email=res['email']
    return render_template("datos.html", id=id,usuario=usuario,email=email)#variable y valor agregado
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Hola Estefany 👋</h1>
    <p>Esta es mi segunda prueba con imagen</p>
    <img src="/static/foto.jpeg" width="400">
    """

if __name__ == "__main__":
    app.run()
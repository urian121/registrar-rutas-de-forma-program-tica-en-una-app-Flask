from flask import Flask
from .routes import registrar_rutas

def create_app():
    app = Flask(__name__)
    registrar_rutas(app)
    return app

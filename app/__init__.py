from flask import Flask
from .config import Config
from .extensions import db, migrate
from app.cliente.routes import cliente_api
from app.funcionario.routes import funcionario_api
from app.produto.routes import produto_api
from app.carrinho.routes import carrinho_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(cliente_api)
    app.register_blueprint(funcionario_api)
    app.register_blueprint(produto_api)
    app.register_blueprint(carrinho_api)

    return app


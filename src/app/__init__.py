from flask import Flask
# from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.app.config import app_config
DB = SQLAlchemy()

def creat_app(environment):
    app = Flask(__name__)
    # DB = SQLAlchemy(app_config)
    # DB.init_app(app)
    # Migrate(app=app, db=DB, directory='./src/app/migrations')

    app.config.from_object(app_config[environment])
    DB.init_app(app)

    # with app.app_context():
    #     # Criar tabelas e popular banco de dados
    #     DB.create_all()
    #     populate_db()

    # from src.app.routes import routes
    # routes(app)

    return app
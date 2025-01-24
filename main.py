from src.app import DB, creat_app
from src.app.routes import routes

from dotenv import load_dotenv
load_dotenv()

app = creat_app()
routes(app)

# def create_tables():
#     with app.app_context():
#         DB.create_all()  # Cria todas as tabelas no banco de dados
#         print("Tabelas criadas com sucesso.")

# # Função para popular o banco de dados automaticamente
# def populate_db():
#     from src.app.db import populate_db
#     with app.app_context():
#         populate_db()  # Chama a função para popular o banco de dados
#         print("Banco de dados populado com sucesso.")

# @click.command(name='create_tables')
# @with_appcontext
# def create_tables():
#     DB.create_all()

# @click.command(name = 'populate_db')
# @with_appcontext
# def call_command():
#   populate_db()

# @click.command(name='delete_tables')
# @with_appcontext
# def delete_tables():
#   DB.drop_all()

# app.cli.add_command(call_command)
# app.cli.add_command(delete_tables)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
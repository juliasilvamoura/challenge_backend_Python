from src.app.models import User, Role
from werkzeug.security import generate_password_hash
from src.app import DB


def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        return user
    except Exception as e:
        return {"error": f"{e}"}

def get_role_by_user(id):
    try:
        role_by_user = DB.session.query(User.id, User.name, User.role_id).filter_by(id=id).first()
        return role_by_user
    except Exception as e:
        return {"error": f"{e}"}

def get_role_by_id(id):
    try:
        role = Role.query.filter_by(id=id).first()
        return role
    except Exception as e:
        return {"error": f"{e}"} 

def create_user(body):
    # Valida se todos os campos obrigatórios estão presentes
    required_fields = ["name", "email", "role_id"]
    for field in required_fields:
        if field not in body:
            return {"error":f"'{field}' is required"}
    
    # Valida se o email já está em uso
    if User.query.filter_by(email=body['email']).first():
        return {"error": "Email already in use"}

    password = body.get("password", "").strip() or body['email']
    hashed_password = generate_password_hash(password)

    new_user = User(
        name=body['name'],
        email=body['email'],
        password=hashed_password,
        role_id=body['role_id']
    )
    DB.session.add(new_user)
    DB.session.commit()
    return new_user
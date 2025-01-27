from src.app.models import User, Role
from werkzeug.security import generate_password_hash
from src.app import DB

def get_role_by_id(id):
    try:
        role = Role.query.filter_by(id=id).first()
        return role
    except Exception as e:
        return {"error": f"{e}"}
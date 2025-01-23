from src.app.utils import is_table_empty
from src.app.models.roles import Role
from src.app.models.users import User
from src.app.models.claims import Claim
from src.app.models.user_claim import UserClaim
from src.app import DB

users = [
    {"name": "João Victor", "email":'joao@email.com',  "password":"password123", "role_id":1},
    {"name": "Pablo Willow", "email":'pablo@email.com', "role_id":2},
    {"name": "Nicoly Moura", "email":'nick@email.com', "role_id":2},
    {"name": "Henrique Marcolino", "email":'marcos@email.com', "role_id":3},
]

roles = [
    {"description" : "SYSTEM_ADMIN"},
    {"description" : "FRONTEND_DEVELOPER"},
    {"description" : "BACKEND_DEVELOPER"},
    {"description" : "COORDINATOR"}
]

claims=[
     {"description": "Read Access"},
     {"description": "Write Access"},
]

user_claims = [
            {"user_id": 1, "claim_id": 1}, 
            {"user_id": 2, "claim_id": 2}, 
            {"user_id": 3, "claim_id": 1}, 
            {"user_id": 4, "claim_id": 2},
        ]

def populate_db_role():
    if is_table_empty(Role.query.first(), 'roles'):
        for role in roles:
            new_role = Role(**role)
            DB.session.add(new_role)
        DB.session.commit()
        print("Roles populated")

def populate_db_user():
    if is_table_empty(User.query.first(), 'users'):
        for user in users:
            new_user = User(**user)
            DB.session.add(new_user)
        DB.session.commit()
        print("Users populated")

def populate_db_claims():
    if is_table_empty(Claim.query.first(), 'claims'):
        for claim in claims:
            new_claim = Claim(**claim)
            DB.session.add(new_claim)
        DB.session.commit()
        print("Users populated")


def populate_db_users_claims():
    if is_table_empty(UserClaim.query.first(), 'claims'):
        for user_claim in user_claims:
            new_user_claim = Claim(**user_claim)
            DB.session.add(new_user_claim)
        DB.session.commit()
        print("Users populated")

def populate_db():
     populate_db_role()
     populate_db_user()
     populate_db_claims()
     populate_db_users_claims()
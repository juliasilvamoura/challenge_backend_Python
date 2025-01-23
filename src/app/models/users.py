from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from src.app import DB

class User(DB.Model):
    __tablename__ = 'users'

    id = DB.Column(DB.BigInteger, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, nullable=False)
    email = DB.Column(DB.String, unique=True, nullable=False)
    password = DB.Column(DB.String, nullable=False)
    role_id = DB.Column(DB.Integer, ForeignKey('roles.id'), nullable=False)
    created_at = DB.Column(DB.DateTime, server_default=func.now(), nullable=False)
    updated_at = DB.Column(DB.DateTime, onupdate=func.now(), nullable=True)

    # Relacionamento com Role - 1 -> N
    role = DB.relationship("Role", back_populates="users")

    # Relacionamento com Claim - N -> N
    claims = DB.relationship(
        "Claim", secondary="user_claims", back_populates="users"
    )

    def __repr__(self) -> str:
        return (f"User(id={self.id}, name={self.name}, email={self.email}, "
                f"role_id={self.role_id}, created_at={self.created_at}, "
                f"updated_at={self.updated_at})")

def as_dict(self):
    return {
        "id": self.id,
        "name": self.name,
        "email": self.email,
        "role_id": self.role_id,
        "created_at": self.created_at.isoformat() if self.created_at else None,
        "updated_at": self.updated_at.isoformat() if self.updated_at else None,
    }
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from src.app import DB

class Role(DB.Model):
    __tablename__ = 'roles'
    id: Mapped[int] = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    description: Mapped[str] = DB.Column(DB.String, nullable=False)
    
    # Relacionamento com o User 
    users: Mapped[list["User"]] = relationship("User", back_populates="role")
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class Claim(DB.Model):
    __tablename__ = 'claims'
    id: Mapped[int] = DB.Column(DB.BigInteger, primary_key=True, autoincrement=True)
    description: Mapped[str] = DB.Column(DB.String, nullable=False)
    active: Mapped[bool] = DB.Column(DB.Boolean, default=True)
    
    # Relacionamento com o UserClaim
    users_claims: Mapped[list["UserClaim"]] = relationship("UserClaim", back_populates="claim")
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class User(DB.Model):
    __tablename__ = 'users'
    id: Mapped[int] = DB.Column(DB.BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = DB.Column(DB.String, nullable=False)
    email: Mapped[str] = DB.Column(DB.String, nullable=False)
    password: Mapped[str] = DB.Column(DB.String, nullable=False)
    role_id: Mapped[int] = DB.Column(DB.Integer, DB.ForeignKey('roles.id'), nullable=False)
    created_at: Mapped[str] = DB.Column(DB.Date, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[str] = DB.Column(DB.Date, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)
    
    # Relacionamento com o Role
    role: Mapped["Role"] = relationship("Role", back_populates="users")
    
    # Relacionamento com o UserClaim
    claims: Mapped[list["UserClaim"]] = relationship("UserClaim", back_populates="user")

    def as_dict(self):
        user_dict = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role_id": self.role_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return user_dict

class UserClaim(DB.Model):
    __tablename__ = 'user_claims'
    user_id: Mapped[int] = DB.Column(DB.BigInteger, DB.ForeignKey('users.id'), primary_key=True)
    claim_id: Mapped[int] = DB.Column(DB.BigInteger, DB.ForeignKey('claims.id'), primary_key=True)
    
    # Relacionamento com o User
    user: Mapped["User"] = relationship("User", back_populates="claims")
    
    # Relacionamento com o Claim
    claim: Mapped["Claim"] = relationship("Claim", back_populates="users_claims")

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
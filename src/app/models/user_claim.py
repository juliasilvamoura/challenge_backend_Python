from sqlalchemy import ForeignKey
from src.app import DB

class UserClaim(DB.Model):
    __tablename__ = 'user_claims'

    user_id = DB.Column(DB.BigInteger, ForeignKey('users.id'), primary_key=True)
    claim_id = DB.Column(DB.BigInteger, ForeignKey('claims.id'), primary_key=True)

    user= DB.relationship("User", back_populates="claims")
    claim= DB.relationship("Claim", back_populates="users")

    def __repr__(self) -> str:
        return f"UserClaim(user_id={self.user_id}, claim_id={self.claim_id})"
from src.app import DB

class Claim(DB.Model):
    __tablename__= 'claims'

    id = DB.Column(DB.BigInteger ,primary_key=True, autoincrement=True)
    description = DB.Column(DB.String, nullable=False)
    active = DB.Column(DB.Boolean, nullable=False, default=True)

     # Relacionamento com User - N -> N
    users= DB.relationship(
        "User", secondary="user_claims", back_populates="claims"
    )

    def __repr__(self) -> str:
        return f"Claim(id={self.id}, description={self.description}, active={self.active})"
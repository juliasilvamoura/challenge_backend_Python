from src.app import DB

class Role(DB.Model):
    __tablename__ = 'roles'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    description = DB.Column(DB.String, nullable=False)

    # Relacionamento com User - N -> 1
    users= DB.relationship("User",back_populates="role")

    # metodo de reprodução
    def __repr__(self) -> str:
        return f"Role(id={self.id}, description={self.description})"
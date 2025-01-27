from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Mapped, aliased
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, Date, Boolean, func
from datetime import date

USERNAME = "root"
PASSWORD = "root"
HOST = "localhost"
PORT = "5432"
DATABASE = "root"

# Criar a conexão com o banco
db = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)
# Factory session
Session = sessionmaker(bind=db)
# instancia da session
session = Session()


Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)

    # Relacionamento com User - N -> 1
    users: Mapped[list["User"]] = relationship(back_populates="role")

    # metodo de reprodução
    def __repr__(self) -> str:
        return f"Role(id={self.id}, description={self.description})"

class Claim(Base):
    __tablename__= 'claims'

    id = Column(BigInteger ,primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)

     # Relacionamento com User - N -> N
    users: Mapped[list["User"]] = relationship(
        "User", secondary="user_claims", back_populates="claims"
    )

    def __repr__(self) -> str:
        return f"Claim(id={self.id}, description={self.description}, active={self.active})"


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(ForeignKey('roles.id'), nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=True)

    # Relacionamento com Role - 1 -> N
    role: Mapped["Role"] = relationship(back_populates="users")

    # Relacionamento com Claim - N -> N
    claims: Mapped[list["Claim"]] = relationship(
        "Claim", secondary="user_claims", back_populates="users"
    )

    def __repr__(self) -> str:
        return (f"User(id={self.id}, name={self.name}, email={self.email}, "
                f"role_id={self.role_id}, created_at={self.created_at}, "
                f"updated_at={self.updated_at})")

class UserClaim(Base):
    __tablename__ = 'user_claims'

    user_id = Column(BigInteger, ForeignKey('users.id'), primary_key=True)
    claim_id = Column(BigInteger, ForeignKey('claims.id'), primary_key=True)

    user: Mapped["User"] = relationship()
    claim: Mapped["Claim"] = relationship()

    def __repr__(self) -> str:
        return f"UserClaim(user_id={self.user_id}, claim_id={self.claim_id})"

Base.metadata.create_all(bind=db)


role_admin = Role(description="Administrator")
role_dev = Role(description="Desenvolvedor")

# Criando uma nova Claim
claim_read = Claim(description="Read Access")
claim_write = Claim(description="Write Access")

# Criando um novo User
user_john = User(
    name="John Doe",
    email="john.doe@example.com",
    password="password123",
    role=role_admin,  # Associando o role
    created_at=date.today()  # Use a data atual aqui
)

user_julia = User(
    name="Julia Moura",
    email="julia.moura@example.com",
    password="password123",
    role=role_dev,  # Associando o role
    created_at=date.today()  # Use a data atual aqui
)

# Associando claims ao User
user_john.claims = [claim_read, claim_write]
user_julia.claims = [claim_read]

# Adicionando as instâncias ao banco de dados
session.add(role_admin)
session.add(claim_read)
session.add(claim_write)
session.add(user_john)
session.add(user_julia)

# Confirmando as transações
session.commit()

# Consulta Questão 2
role_alias = aliased(Role)
claim_alias = aliased(Claim)

query = session.query(
    User.name.label('name_user'),
    User.email.label('email_user'),
    role_alias.description.label('description_role'),
    func.string_agg(claim_alias.description, ', ').label('description_claims')
).join(
    role_alias, role_alias.id == User.role_id  # Usando o alias
).outerjoin(
    UserClaim, UserClaim.user_id == User.id
).outerjoin(
    claim_alias, claim_alias.id == UserClaim.claim_id  # Usando o alias
).group_by(
    User.id, User.name, User.email, role_alias.description
).order_by(
    User.name.asc()
)

results = query.all()

for result in results:
    print(result)

# Fechando a sessão
session.close()
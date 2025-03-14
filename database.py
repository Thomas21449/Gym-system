from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from crypto_manager import CryptoManager

# Configuração do banco de dados
DATABASE_URL = "sqlite:///gym.db"  # Exemplo para SQLite
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Carregar ou gerar a chave de criptografia
try:
    crypto = CryptoManager(key=CryptoManager.load_key())
except FileNotFoundError:
    crypto = CryptoManager()
    crypto.save_key()

# Modelo de Membro
class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Nome criptografado
    email = Column(String, unique=True, nullable=False)  # E-mail criptografado
    plan = Column(String, nullable=False)
    monthly_access_limit = Column(Integer, default=8)
    access_count = Column(Integer, default=0)
    last_access_date = Column(Date)
    active = Column(Boolean, default=True)
    access_frequency = Column(String, nullable=False)

    def set_name(self, name):
        """Criptografa e define o nome."""
        self.name = crypto.encrypt(name).decode()

    def get_name(self):
        """Descriptografa e retorna o nome."""
        return crypto.decrypt(self.name.encode())

    def set_email(self, email):
        """Criptografa e define o e-mail."""
        self.email = crypto.encrypt(email).decode()

    def get_email(self):
        """Descriptografa e retorna o e-mail."""
        return crypto.decrypt(self.email.encode())

# Modelo de Produto
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

# Modelo de Venda
class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    quantity = Column(Integer, nullable=False)
    payment_method = Column(String, nullable=False)
    sale_date = Column(Date, default=datetime.today().date())

# Criação das tabelas (se necessário)
Base.metadata.create_all(bind=engine)

# Sessão para uso no código
session = SessionLocal()
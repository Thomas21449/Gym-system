from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    facial_data = Column(String)  # Caminho da imagem ou hash
    plan = Column(String)
    payment_status = Column(String)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)
    total = Column(Float)
    payment_method = Column(String)

# Configuração do banco de dados
engine = create_engine('sqlite:///gym.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
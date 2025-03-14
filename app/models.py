from app import db
from datetime import datetime

class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    plan = db.Column(db.String(50), nullable=False)
    monthly_access_limit = db.Column(db.Integer, default=8)
    access_count = db.Column(db.Integer, default=0)
    last_access_date = db.Column(db.Date)
    active = db.Column(db.Boolean, default=True)
    access_frequency = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Member {self.name}>"

# Outros modelos (Product, Sale, etc.) podem ser adicionados aqui
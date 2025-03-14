from datetime import datetime
from database import session, Member, Product, Sale
from crypto_manager import CryptoManager

class GymManager:
    def __init__(self):
        self.access_limits = {
            "Mensal": 8,    # 2x por semana
            "Semestral": 12,  # 3x por semana
            "Anual": 20,     # Diário
        }
        self.crypto = CryptoManager()

    def add_member(self, name, email, plan, access_frequency):
        """
        Adiciona um novo aluno com dados criptografados.
        """
        member = Member(
            name=self.crypto.encrypt(name).decode(),
            email=self.crypto.encrypt(email).decode(),
            plan=plan,
            monthly_access_limit=self.access_limits.get(plan, 8),
            access_frequency=access_frequency,
        )
        session.add(member)
        session.commit()
        return member.id

    def list_members(self, filter_type="ativos"):
        """
        Lista os alunos com dados descriptografados.
        """
        query = session.query(Member)
        if filter_type == "ativos":
            query = query.filter_by(active=True)
        elif filter_type == "inativos":
            query = query.filter_by(active=False)
        elif filter_type == "especifico":
            # Implemente a lógica para buscar um aluno específico
            pass
        elif filter_type != "todos":
            print("Filtro inválido.")
            return

        members = query.all()
        for member in members:
            member.name = self.crypto.decrypt(member.name.encode())
            member.email = self.crypto.decrypt(member.email.encode())
        return members

    # Outros métodos (add_product, list_products, sell_product, etc.)
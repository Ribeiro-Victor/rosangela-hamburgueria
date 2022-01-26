from app.extensions import db
from app.models import BaseModel

class Cliente(BaseModel):
    
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(15), nullable=False)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(20))
    telefone = db.Column(db.String(20))
    endereco = db.Column(db.String(70))

    carrinho = db.relationship("Carrinho", back_populates="cliente", uselist=False)

    def json(self):
        return {
            "id":self.id,
            "cpf":self.cpf,
            "nome":self.nome,
            "email":self.email,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "senha":self.senha
        }
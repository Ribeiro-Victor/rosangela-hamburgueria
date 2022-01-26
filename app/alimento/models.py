from app.extensions import db
from app.models import BaseModel

class Alimento(BaseModel):

    __tablename__ = 'alimento'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20))
    descricao = db.Column(db.String(20))
    quantidade = db.Column(db.Integer)

    def json(self):
        return {
            "nome":self.nome,
            "descricao":self.descricao,
            "quantidade":self.quantidade
        }
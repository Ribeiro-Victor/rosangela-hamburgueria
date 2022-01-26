from app.extensions import db
from app.models import BaseModel

class Produto(BaseModel):

    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20))
    descricao = db.Column(db.String(20))
    preco = db.Column(db.Float)
    

    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "descricao":self.descricao,
            "preco":self.preco
        }
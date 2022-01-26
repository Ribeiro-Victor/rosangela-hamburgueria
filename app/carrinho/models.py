from app.extensions import db
from app.models import BaseModel

class Carrinho(BaseModel):

    __tablename__ = 'carrinho'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    precoTotal = db.Column(db.Float)
    #adicionar relacao com produtos
    #adicionar relacao com cliente

    def json(self):
        return {
            "precoTotal":self.precoTotal,

        }
from app.extensions import db
from app.models import BaseModel
from app.association import association_carrinho_produto

class Carrinho(BaseModel):

    __tablename__ = 'carrinho'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    precoTotal = db.Column(db.Float)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    cliente = db.relationship("Cliente", back_populates="carrinho")
    produtos = db.relationship("Produto", secondary=association_carrinho_produto)

    def json(self):
        return {
            "id":self.id,
            "precoTotal":self.precoTotal,
            "id_cliente":self.id_cliente,
            "produtos":self.produtos
        }
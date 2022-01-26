from app.extensions import db
from app.usuario.models import BaseModel

class Produto(BaseModel):

    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    descricao = db.Column(db.String(20))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    

    def json(self):
        return {
            
        }
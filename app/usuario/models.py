from app.extensions import db
from app.usuario.models import BaseModel

class Usuario(BaseModel):
    
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    cpf = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(70))
    email = db.Column(db.String(70), unique=True, index=True)

    pedidos = db.relationship('pedido')

    def json(self):
        return {
            "cpf":self.cpf,
            "name":self.name,
            "id":self.id,
            "email":self.email
        }
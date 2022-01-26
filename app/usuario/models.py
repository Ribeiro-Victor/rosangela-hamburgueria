from app.extensions import db
from app.usuario.models import BaseModel

class Usuario(BaseModel):
    
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    cpf = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(50))
    telefone = db.Column(db.String(20), unique=True, index=True)
    endereco = db.Column(db.String(70))
    email = db.Column(db.String(50))


    def json(self):
        return {
            "cpf":self.cpf,
            "name":self.name,
            "id":self.id,
            "email":self.email,
            "endereco": self.endereco,
            "telefone": self.telefone
        }
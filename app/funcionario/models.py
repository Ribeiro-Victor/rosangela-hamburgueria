from app.extensions import db
from app.models import BaseModel

class Funcionario(BaseModel):

    __tablename__ = 'funcionario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(20))

    def json(self):
        return {
            "nome":self.nome,
            "email":self.email
        }
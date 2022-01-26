from app.extensions import db

association_carrinho_produto = db.Table('association', 
        db.Column('carrinho_id', db.Integer, db.ForeignKey('carrinho.id')),
        db.Column('produto_id', db.Integer, db.ForeignKey('produto.id')),
        db.Column('quantidade_produto', db.Integer)
        )
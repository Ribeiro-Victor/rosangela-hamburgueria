from .extensions import db

class BaseModel(db.Model):
    
    __abstract__ = True

    create_time = db.Column(db.String)
    update_time = db.Column(db.String)

    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    

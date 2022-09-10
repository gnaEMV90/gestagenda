from app import db

class Plantilla(db.Model):
    __tablename__ = 'plantillas'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255))
    tipo = db.Column(db.String(255))
    detalle = db.Column(db.Text())
    
    
    def __init__(self, titulo, tipo, detalle) -> None:
        self.titulo = titulo
        self.tipo = tipo
        self.detalle = detalle
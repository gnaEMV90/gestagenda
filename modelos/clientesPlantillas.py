from app import db

class ClientesPlantillas(db.Model):
    __tablename__ = 'clientesplantillas'
    id = db.Column(db.Integer, primary_key=True)
    idCliente = db.Column(db.Integer)
    idPlantilla = db.Column(db.Integer)
    
    def __init__(self, idcliente, idplantilla) -> None:
        self.idCliente = idcliente
        self.idPlantilla = idplantilla
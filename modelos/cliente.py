from app import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    nacimiento = db.Column(db.Date())
    documento = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    localidad = db.Column(db.String(255))
    provincia = db.Column(db.String(255))
    telefono = db.Column(db.String(255))
    email = db.Column(db.String(255))
    tipoCliente = db.Column(db.String(255))
    obraSocial = db.Column(db.String(255))
    nroAfiliado = db.Column(db.String(255))
    notas = db.Column(db.Text())
    peso = db.Column(db.String(255))
    altura = db.Column(db.String(255))
    
    def __init__(self, nombre, apellido, nacimiento, documento, direccion, localidad, provincia, telefono, email, tipoCliente, obraSocial, nroAfiliado, notas, peso, altura) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.documento = documento
        self.direccion = direccion
        self.localidad = localidad
        self.provincia = provincia  
        self.telefono = telefono
        self.email = email
        self.tipoCliente = tipoCliente
        self.obraSocial = obraSocial
        self.nroAfiliado = nroAfiliado
        self.notas = notas
        self.peso = peso
        self.altura = altura
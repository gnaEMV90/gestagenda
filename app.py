
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

#Configuración
app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dbOwner@localhost/agenda'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev'
else:
    app.debug = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.config['SECRET_KEY'] = 'pro'

db = SQLAlchemy(app)

#Clases
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
    peso = db.Column(db.String(255))
    altura = db.Column(db.String(255))
    vigente = db.Column(db.String(2))

    
    def __init__(self, nombre, apellido, nacimiento, documento, direccion, localidad, provincia, telefono, email, tipoCliente, obraSocial, nroAfiliado, peso, altura, vigente) -> None:
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
        self.peso = peso
        self.altura = altura
        self.vigente = vigente

class Plan(db.Model):
    __tablename__ = 'planes'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255))
    tipo = db.Column(db.String(255))
    detalle = db.Column(db.Text())
    vigente = db.Column(db.String(2))
    
    def __init__(self, titulo, tipo, detalle, vigente) -> None:
        self.titulo = titulo
        self.tipo = tipo
        self.detalle = detalle
        self.vigente = vigente

class Clientesplanes(db.Model):
    __tablename__ = 'clientesplanes'
    id = db.Column(db.Integer, primary_key=True)
    idCliente = db.Column(db.Integer)
    idPlan = db.Column(db.Integer)
    fechainicio = db.Column(db.Date())
    fechafin = db.Column(db.Date())
    
    def __init__(self, idcliente, idPlan, fechainicio, fechafin) -> None:
        self.idCliente = idcliente
        self.idPlan = idPlan
        self.fechainicio = fechainicio
        self.fechafin= fechafin

#Rutas - Inicio
@app.route('/')
def index():
    return render_template('index.html')

#Perfil - FAQ
@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/ayuda')
def faq():
    return render_template('faq.html')

#Clientes
@app.route('/clientes')
def clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes = clientes)

@app.route('/nuevoCliente', methods=['POST'])
def nuevoCliente():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        apellido = request.form['txtApellido']
        nacimiento = request.form['dtNacimiento']
        documento = request.form['txtDocumento']        
        direccion = request.form['txtDireccion']
        localidad = request.form['txtLocalidad']
        provincia = request.form['txtProvincia']
        telefono = request.form['txtTelefono']
        email = request.form['txtEmail']
        tipoCliente = request.form['cmbTipoPaciente']
        obraSocial = request.form['txtObraSocial']
        nroAfiliado = request.form['txtNroAfiliado']
        peso = request.form['txtPeso']
        altura = request.form['txtAltura']
        vigente = request.form['cmbVigente']
        if db.session.query(Cliente).filter(Cliente.documento == documento).count() == 1:
            flash('El cliente ya se encuentra cargado', 'error')
            return redirect(url_for('clientes'))
        data = Cliente(nombre, apellido, nacimiento, documento, direccion, localidad, provincia, telefono, email, tipoCliente, obraSocial, nroAfiliado, peso, altura, vigente)
        db.session.add(data)
        db.session.commit()
        flash('Nuevo Cliente agregado correctamente!', 'success')
        return redirect(url_for('clientes'))

@app.route('/editacliente/<string:id>', methods=["GET", "POST"])
def editacliente(id):
    cliente = Cliente.query.get(id)
    if request.method == 'POST':
        cliente.nombre = request.form['txtNombre']
        cliente.apellido = request.form['txtApellido']
        cliente.nacimiento = request.form['dtNacimiento']
        cliente.documento = request.form['txtDocumento']        
        cliente.direccion = request.form['txtDireccion']
        cliente.localidad = request.form['txtLocalidad']
        cliente.provincia = request.form['txtProvincia']
        cliente.telefono = request.form['txtTelefono']
        cliente.email = request.form['txtEmail']
        cliente.tipoCliente = request.form['cmbTipoPaciente']
        cliente.obraSocial = request.form['txtObraSocial']
        cliente.nroAfiliado = request.form['txtNroAfiliado']
        cliente.peso = request.form['txtPeso']
        cliente.altura = request.form['txtAltura']
        cliente.vigente = request.form['cmbVigente']
        db.session.commit()
        return redirect(url_for('clientes'))
    return render_template("editacliente.html", cliente = cliente)

@app.route('/vercliente/<string:id>', methods=["GET", "POST"])
def vercliente(id):
    cliente = Cliente.query.get(id)
    if request.method == 'POST':
        cliente.nombre = request.form['txtNombre']
        cliente.apellido = request.form['txtApellido']
        cliente.nacimiento = request.form['dtNacimiento']
        cliente.documento = request.form['txtDocumento']        
        cliente.direccion = request.form['txtDireccion']
        cliente.localidad = request.form['txtLocalidad']
        cliente.provincia = request.form['txtProvincia']
        cliente.telefono = request.form['txtTelefono']
        cliente.email = request.form['txtEmail']
        cliente.tipoCliente = request.form['cmbTipoPaciente']
        cliente.obraSocial = request.form['txtObraSocial']
        cliente.nroAfiliado = request.form['txtNroAfiliado']
        cliente.peso = request.form['txtPeso']
        cliente.altura = request.form['txtAltura']
        cliente.vigente = request.form['cmbVigente']
        return redirect(url_for('clientes'))
    return render_template("vercliente.html", cliente = cliente)

#Planes
@app.route('/planes')
def planes():
    planes = Plan.query.all()
    return render_template('planes.html',  planes = planes)

@app.route('/nuevoPlan', methods=['POST'])
def nuevoPlan():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        tipo = request.form['cmbTipo']
        detalle = request.form['txtDetalle']
        vigente = request.form['cmbVigente']
        if db.session.query(Plan).filter(Plan.titulo == titulo,  Plan.tipo == tipo).count() == 1:
            flash('El Plan ya se encuentra cargado.', 'error')
            return redirect(url_for('planes'))
        data = Plan(titulo, tipo, detalle, vigente)
        db.session.add(data)
        db.session.commit()
        flash('Plan agregado correctamente.', 'success')
    return redirect(url_for('planes'))

@app.route('/editaPlan/<string:id>', methods=["GET", "POST"])
def editaPlan(id):
    plan = Plan.query.get(id)
    if request.method == 'POST':
        plan.titulo = request.form['txtTitulo']
        plan.tipo = request.form['cmbTipo']
        plan.detalle = request.form['txtDetalle']
        plan.vigente = request.form['cmbVigente']
        db.session.commit()
        return redirect(url_for('planes'))
    return render_template("editaPlan.html", plan = plan)

@app.route('/eliminaPlan/<string:id>')
def eliminaPlan(id):
    #count1 =  db.session.query(Clientesplanes).filter(Clientesplanes.idPlan == id).first()
    #count = db.session.query(Clientesplanes.query.filter(Clientesplanes.idPlan == id).exists()).scalar()
    print(id)
    if db.session.query(Clientesplanes.query.filter(Clientesplanes.idPlan == id).exists()).scalar() == 0:
        plan = Plan.query.get(id)
        db.session.delete(plan)
        db.session.commit()
        flash('Plan eliminada correctamente.', 'success')
        return redirect(url_for('planes'))
    flash('La Plan no se puede eliminar, ya que está asociada a pacientes.', 'error')
    return redirect(url_for('planes'))

def status_401(error):
    return redirect(url_for('index'))

def status_404(error):
    return render_template("404.html") 

def status_405(error):
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.register_error_handler(405, status_405)
    app.run()

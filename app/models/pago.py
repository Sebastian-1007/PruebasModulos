from app import db

class Pago(db.Model):
    __tablename__ = 'pagos'
    id = db.Column(db.Integer, primary_key=True)
    aspirante_id = db.Column(db.Integer, db.ForeignKey('aspirantes.id'))
    referencia = db.Column(db.String(50))
    monto = db.Column(db.Numeric(10,2))
    estatus = db.Column(db.String(20), default='Pendiente')
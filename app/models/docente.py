from app import db
from datetime import datetime

class Docente(db.Model):
    __tablename__ = 'docentes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    paterno = db.Column(db.String(100), nullable=False)
    materno = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    grado_academico = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con Usuario - usa back_populates en lugar de backref
    usuario_rel = db.relationship('Usuario', back_populates='docente_rel', uselist=False, lazy=True)
    
    def __repr__(self):
        return f'<Docente {self.nombre} {self.paterno}>'
from app import db
from datetime import datetime

class Directivo(db.Model):
    __tablename__ = 'directivos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    paterno = db.Column(db.String(100), nullable=False)
    materno = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    puesto = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con Usuario - usa back_populates en lugar de backref
    usuario_rel = db.relationship('Usuario', back_populates='directivo_rel', uselist=False, lazy=True)
    
    def __repr__(self):
        return f'<Directivo {self.nombre} {self.paterno}>'
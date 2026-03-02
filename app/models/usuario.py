from app import db
from flask_login import UserMixin
from datetime import datetime

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Enum('aspirante', 'docente', 'directivo'), nullable=False, default='aspirante')
    activo = db.Column(db.Boolean, default=True)
    
    # Llaves foráneas
    aspirante_id = db.Column(db.Integer, db.ForeignKey('aspirantes.id', ondelete='CASCADE'), nullable=True)
    docente_id = db.Column(db.Integer, db.ForeignKey('docentes.id', ondelete='CASCADE'), nullable=True)
    directivo_id = db.Column(db.Integer, db.ForeignKey('directivos.id', ondelete='CASCADE'), nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relaciones - SIN backref para evitar conflictos
    aspirante_rel = db.relationship('Aspirante', back_populates='usuario_rel', lazy=True)
    docente_rel = db.relationship('Docente', back_populates='usuario_rel', lazy=True)
    directivo_rel = db.relationship('Directivo', back_populates='usuario_rel', lazy=True)
    
    def get_id(self):
        """Flask-Login requiere este método"""
        return str(self.id)
    
    def get_nombre_completo(self):
        if self.rol == 'aspirante' and self.aspirante_rel:
            return f"{self.aspirante_rel.nombre} {self.aspirante_rel.paterno} {self.aspirante_rel.materno}"
        elif self.rol == 'docente' and self.docente_rel:
            return f"{self.docente_rel.nombre} {self.docente_rel.paterno} {self.docente_rel.materno}"
        elif self.rol == 'directivo' and self.directivo_rel:
            return f"{self.directivo_rel.nombre} {self.directivo_rel.paterno} {self.directivo_rel.materno}"
        return "Usuario"
    
    def get_detalle_rol(self):
        if self.rol == 'docente' and self.docente_rel:
            return self.docente_rel.grado_academico
        elif self.rol == 'directivo' and self.directivo_rel:
            return self.directivo_rel.puesto
        elif self.rol == 'aspirante' and self.aspirante_rel:
            return self.aspirante_rel.programa
        return ""
    
    def es_admin(self):
        return self.rol == 'directivo' and self.correo == 'admin@escuela.edu.mx'
    
    def __repr__(self):
        return f'<Usuario {self.correo} - {self.rol}>'
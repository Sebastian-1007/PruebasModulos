import random
import string
from datetime import datetime
from app import db
from app.models.aspirante import Aspirante

def generar_consecutivo():
    ultimo = db.session.query(db.func.max(Aspirante.consecutivo)).scalar()
    return 1000 if not ultimo else ultimo + 1

def generar_folio():
    """Genera un folio aleatorio de 8 caracteres alfanuméricos"""
    while True:
        letras1 = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeros = ''.join(random.choices(string.digits, k=4))
        letras2 = ''.join(random.choices(string.ascii_uppercase, k=2))
        folio = f"{letras1}{numeros}{letras2}"
        
        existe = Aspirante.query.filter_by(folio=folio).first()
        if not existe:
            return folio

def generar_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def generar_referencia(consecutivo):
    return f"BBVA{datetime.now().year}{consecutivo}"
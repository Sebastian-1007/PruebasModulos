from flask import Blueprint, render_template
from flask_login import login_required, current_user

directivo_bp = Blueprint('directivo', __name__, url_prefix='/directivo')

@directivo_bp.before_request
@login_required
def verificar_directivo():
    """Verifica que el usuario sea directivo"""
    if current_user.rol != 'directivo':
        return render_template('errors/403.html'), 403

@directivo_bp.route('/dashboard')
def dashboard():
    """Dashboard del directivo"""
    return render_template('directivo/dashboard.html')
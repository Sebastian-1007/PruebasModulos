from flask import Blueprint, render_template
from flask_login import login_required, current_user

docente_bp = Blueprint('docente', __name__, url_prefix='/docente')

@docente_bp.before_request
@login_required
def verificar_docente():
    """Verifica que el usuario sea docente"""
    if current_user.rol != 'docente':
        return render_template('errors/403.html'), 403

@docente_bp.route('/dashboard')
def dashboard():
    """Dashboard del docente"""
    return render_template('docente/dashboard.html')
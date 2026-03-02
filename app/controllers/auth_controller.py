from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from app import bcrypt, db
from app.models.usuario import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')
        
        # Buscar usuario por correo
        user = Usuario.query.filter_by(correo=correo).first()
        
        if user and bcrypt.check_password_hash(user.password_hash, password):
            if not user.activo:
                flash('Tu cuenta está desactivada. Contacta al administrador.', 'danger')
                return render_template('login.html')
            
            # Iniciar sesión
            login_user(user)
            
            # Redirigir según el rol
            if user.rol == 'docente':
                return redirect(url_for('docente.dashboard'))
            elif user.rol == 'directivo':
                # Verificar si es admin
                if user.correo == 'admin@escuela.edu.mx':
                    return redirect(url_for('admin.dashboard'))
                return redirect(url_for('directivo.dashboard'))
            else:  # aspirante
                return redirect(url_for('pdf.dashboard'))  # Tu dashboard existente
        else:
            flash('Correo o contraseña incorrectos', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('Sesión cerrada correctamente', 'success')
    return redirect(url_for('auth.login'))
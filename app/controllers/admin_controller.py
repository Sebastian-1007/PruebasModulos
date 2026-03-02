from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db, bcrypt
from app.models.usuario import Usuario
from app.models.docente import Docente
from app.models.directivo import Directivo
import secrets
import string

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def generar_contraseña(longitud=10):
    """Genera una contraseña aleatoria segura"""
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

def generar_correo(nombre, paterno, rol):
    """Genera un correo institucional"""
    nombre_limpio = nombre.lower().replace(' ', '.')
    paterno_limpio = paterno.lower().replace(' ', '.')
    if rol == 'docente':
        return f"{nombre_limpio}.{paterno_limpio}@docente.escuela.edu.mx"
    else:
        return f"{nombre_limpio}.{paterno_limpio}@directivo.escuela.edu.mx"

@admin_bp.before_request
@login_required
def verificar_admin():
    """Verifica que el usuario sea admin antes de acceder a cualquier ruta"""
    if current_user.rol != 'directivo' or current_user.correo != 'admin@escuela.edu.mx':
        flash('Acceso no autorizado', 'danger')
        return redirect(url_for('auth.login'))

@admin_bp.route('/dashboard')
def dashboard():
    """Dashboard del administrador"""
    # Estadísticas
    total_docentes = Usuario.query.filter_by(rol='docente').count()
    total_directivos = Usuario.query.filter_by(rol='directivo').count()
    total_aspirantes = Usuario.query.filter_by(rol='aspirante').count()
    
    # Últimos usuarios creados
    ultimos_usuarios = Usuario.query.order_by(Usuario.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html', 
                         total_docentes=total_docentes,
                         total_directivos=total_directivos,
                         total_aspirantes=total_aspirantes,
                         ultimos_usuarios=ultimos_usuarios)

@admin_bp.route('/crear-docente', methods=['GET', 'POST'])
def crear_docente():
    """Vista para crear un nuevo docente"""
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            nombre = request.form['nombre']
            paterno = request.form['paterno']
            materno = request.form['materno']
            telefono = request.form['telefono']
            grado_academico = request.form['grado_academico']
            
            # Generar correo y contraseña
            correo = generar_correo(nombre, paterno, 'docente')
            contraseña = generar_contraseña()
            
            # Verificar si el correo ya existe
            if Usuario.query.filter_by(correo=correo).first():
                base_correo = correo.split('@')[0]
                contador = 1
                while Usuario.query.filter_by(correo=correo).first():
                    correo = f"{base_correo}{contador}@docente.escuela.edu.mx"
                    contador += 1
            
            # Crear el docente en la tabla docentes
            docente = Docente(
                nombre=nombre,
                paterno=paterno,
                materno=materno,
                telefono=telefono,
                grado_academico=grado_academico
            )
            db.session.add(docente)
            db.session.flush()  # Para obtener el ID del docente
            
            # Crear el usuario
            usuario = Usuario(
                correo=correo,
                password_hash=bcrypt.generate_password_hash(contraseña).decode('utf-8'),
                rol='docente',
                docente_id=docente.id,
                activo=True
            )
            db.session.add(usuario)
            db.session.commit()
            
            # Mostrar las credenciales al admin
            flash(f'Docente creado exitosamente', 'success')
            flash(f'Correo: {correo}', 'info')
            flash(f'Contraseña: {contraseña}', 'warning')
            flash('¡Guarda estas credenciales para entregarlas al docente!', 'info')
            
            return redirect(url_for('admin.dashboard'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear el docente: {str(e)}', 'danger')
    
    return render_template('admin/crear_docente.html')

@admin_bp.route('/crear-directivo', methods=['GET', 'POST'])
def crear_directivo():
    """Vista para crear un nuevo directivo"""
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            nombre = request.form['nombre']
            paterno = request.form['paterno']
            materno = request.form['materno']
            telefono = request.form['telefono']
            puesto = request.form['puesto']
            
            # Generar correo y contraseña
            correo = generar_correo(nombre, paterno, 'directivo')
            contraseña = generar_contraseña()
            
            # Verificar si el correo ya existe
            if Usuario.query.filter_by(correo=correo).first():
                base_correo = correo.split('@')[0]
                contador = 1
                while Usuario.query.filter_by(correo=correo).first():
                    correo = f"{base_correo}{contador}@directivo.escuela.edu.mx"
                    contador += 1
            
            # Crear el directivo en la tabla directivos
            directivo = Directivo(
                nombre=nombre,
                paterno=paterno,
                materno=materno,
                telefono=telefono,
                puesto=puesto
            )
            db.session.add(directivo)
            db.session.flush()  # Para obtener el ID del directivo
            
            # Crear el usuario
            usuario = Usuario(
                correo=correo,
                password_hash=bcrypt.generate_password_hash(contraseña).decode('utf-8'),
                rol='directivo',
                directivo_id=directivo.id,
                activo=True
            )
            db.session.add(usuario)
            db.session.commit()
            
            # Mostrar las credenciales al admin
            flash(f'Directivo creado exitosamente', 'success')
            flash(f'Correo: {correo}', 'info')
            flash(f'Contraseña: {contraseña}', 'warning')
            flash('¡Guarda estas credenciales para entregarlas al directivo!', 'info')
            
            return redirect(url_for('admin.dashboard'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear el directivo: {str(e)}', 'danger')
    
    return render_template('admin/crear_directivo.html')
@admin_bp.route('/listar-docentes')
def listar_docentes():
    """Lista todos los docentes registrados"""
    docentes = Usuario.query.filter_by(rol='docente').all()
    return render_template('admin/listar_docentes.html', docentes=docentes)

@admin_bp.route('/listar-directivos')
def listar_directivos():
    """Lista todos los directivos registrados"""
    directivos = Usuario.query.filter_by(rol='directivo').all()
    return render_template('admin/listar_directivos.html', directivos=directivos)
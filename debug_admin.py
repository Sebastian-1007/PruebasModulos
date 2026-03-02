# debug_admin.py
from app import create_app, db, bcrypt
from app.models.usuario import Usuario
from app.models.directivo import Directivo
import sys

def debug_admin():
    print("=" * 50)
    print("🔍 DIAGNÓSTICO DE ADMIN")
    print("=" * 50)
    
    app = create_app()
    with app.app_context():
        # 1. Verificar todos los usuarios
        print("\n📋 1. USUARIOS EN LA BASE DE DATOS:")
        print("-" * 40)
        usuarios = Usuario.query.all()
        if not usuarios:
            print("❌ No hay usuarios registrados")
        else:
            for u in usuarios:
                print(f"ID: {u.id}")
                print(f"Correo: {u.correo}")
                print(f"Rol: {u.rol}")
                print(f"Activo: {u.activo}")
                print(f"Directivo ID: {u.directivo_id}")
                print(f"Docente ID: {u.docente_id}")
                print(f"Aspirante ID: {u.aspirante_id}")
                print("-" * 30)
        
        # 2. Buscar específicamente admin
        print("\n🔍 2. BUSCANDO USUARIO ADMIN:")
        print("-" * 40)
        
        # Buscar por correos comunes
        correos_admin = [
            'admin@escuela.edu.mx',
            'administrador@escuela.edu.mx',
            'admin@localhost',
            'admin@admin.com'
        ]
        
        admin_encontrado = None
        for correo in correos_admin:
            user = Usuario.query.filter_by(correo=correo).first()
            if user:
                print(f"✅ Encontrado: {correo}")
                admin_encontrado = user
                break
        
        if not admin_encontrado:
            print("❌ No se encontró ningún usuario con correos de admin")
            # Buscar cualquier usuario con rol directivo
            directivos = Usuario.query.filter_by(rol='directivo').all()
            if directivos:
                print(f"\n📌 Se encontraron {len(directivos)} directivos:")
                for d in directivos:
                    print(f"   - {d.correo}")
        
        # 3. Verificar contraseña del admin encontrado
        if admin_encontrado:
            print(f"\n🔐 3. VERIFICANDO CONTRASEÑA:")
            print("-" * 40)
            contraseñas_probar = ['Admin123!', 'admin123', 'admin', '123456']
            
            for pwd in contraseñas_probar:
                if bcrypt.check_password_hash(admin_encontrado.password_hash, pwd):
                    print(f"✅ Contraseña correcta: {pwd}")
                    print(f"   Hash: {admin_encontrado.password_hash}")
                else:
                    print(f"❌ Contraseña incorrecta: {pwd}")
        
        # 4. Verificar relaciones
        if admin_encontrado and admin_encontrado.directivo_id:
            print(f"\n👤 4. VERIFICANDO RELACIÓN CON DIRECTIVO:")
            print("-" * 40)
            directivo = Directivo.query.get(admin_encontrado.directivo_id)
            if directivo:
                print(f"✅ Directivo encontrado:")
                print(f"   Nombre: {directivo.nombre} {directivo.paterno} {directivo.materno}")
                print(f"   Puesto: {directivo.puesto}")
                print(f"   Teléfono: {directivo.telefono}")
            else:
                print(f"❌ No se encontró directivo con ID: {admin_encontrado.directivo_id}")
        
        # 5. Probar el método es_admin() del modelo
        if admin_encontrado:
            print(f"\n🎯 5. PROBANDO MÉTODO es_admin():")
            print("-" * 40)
            print(f"Resultado: {admin_encontrado.es_admin()}")
            print(f"Rol: {admin_encontrado.rol}")
            print(f"Correo: {admin_encontrado.correo}")
        
        # 6. Crear un admin nuevo si no existe
        if not admin_encontrado:
            print(f"\n🆕 6. CREANDO NUEVO ADMIN:")
            print("-" * 40)
            try:
                # Crear directivo
                nuevo_directivo = Directivo(
                    nombre='Admin',
                    paterno='Sistema',
                    materno='Root',
                    telefono='555-000-0000',
                    puesto='Administrador del Sistema'
                )
                db.session.add(nuevo_directivo)
                db.session.flush()
                
                # Crear usuario con contraseña 'Admin123!'
                password = 'Admin123!'
                password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
                
                nuevo_usuario = Usuario(
                    correo='admin@escuela.edu.mx',
                    password_hash=password_hash,
                    rol='directivo',
                    directivo_id=nuevo_directivo.id,
                    activo=True
                )
                db.session.add(nuevo_usuario)
                db.session.commit()
                
                print(f"✅ Admin creado exitosamente!")
                print(f"   Correo: admin@escuela.edu.mx")
                print(f"   Contraseña: {password}")
                print(f"   Hash: {password_hash}")
                
            except Exception as e:
                print(f"❌ Error al crear admin: {str(e)}")
                db.session.rollback()

if __name__ == '__main__':
    debug_admin()
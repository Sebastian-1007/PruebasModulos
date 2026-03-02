# update_admin_password.py
from app import create_app, bcrypt
from app.models.usuario import Usuario
from app import db

def update_admin_password():
    print("🔄 Actualizando contraseña del admin...")
    
    app = create_app()
    with app.app_context():
        # Buscar el admin
        admin = Usuario.query.filter_by(correo='admin@escuela.edu.mx').first()
        
        if admin:
            # Nueva contraseña
            nueva_password = 'Admin123!'
            nueva_password_hash = bcrypt.generate_password_hash(nueva_password).decode('utf-8')
            
            print(f"✅ Admin encontrado: {admin.correo}")
            print(f"   ID: {admin.id}")
            print(f"   Rol: {admin.rol}")
            print(f"   Hash actual: {admin.password_hash}")
            
            # Actualizar
            admin.password_hash = nueva_password_hash
            db.session.commit()
            
            print(f"\n✅ CONTRASEÑA ACTUALIZADA:")
            print(f"   Correo: admin@escuela.edu.mx")
            print(f"   Nueva contraseña: {nueva_password}")
            print(f"   Nuevo hash: {nueva_password_hash}")
            
            # Verificar
            if bcrypt.check_password_hash(admin.password_hash, nueva_password):
                print("✅ Verificación: Contraseña correcta")
            else:
                print("❌ Verificación: Error en la contraseña")
        else:
            print("❌ No se encontró el admin con correo: admin@escuela.edu.mx")
            
            # Listar todos los directivos por si acaso
            print("\n📋 Directivos disponibles:")
            directivos = Usuario.query.filter_by(rol='directivo').all()
            for d in directivos:
                print(f"   - {d.correo}")

if __name__ == '__main__':
    update_admin_password()
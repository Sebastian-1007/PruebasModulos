# test_db.py
import oracledb
from config import Config

def test_connection():
    try:
        # ❌ ELIMINA esta línea - NO la necesitas
        # oracledb.init_oracle_client()
        
        # ✅ Conexión directa en modo Thin
        connection = oracledb.connect(
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            dsn=Config.TNS_NAME,
            config_dir=Config.WALLET_PATH,
            wallet_location=Config.WALLET_PATH,
            wallet_password=Config.WALLET_PASSWORD
        )
        
        print("✅ ¡CONEXIÓN EXITOSA a Oracle Cloud!")
        
        # Probar con una consulta simple
        cursor = connection.cursor()
        cursor.execute("SELECT 'Hola Oracle Cloud' FROM DUAL")
        result = cursor.fetchone()
        print(f"📝 Consulta de prueba: {result[0]}")
        print(f"📌 Modo Thin: {connection.thin}")  # Debe decir True
        
        cursor.close()
        connection.close()
        print("🔌 Conexión cerrada correctamente")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR de conexión: {e}")
        return False

if __name__ == "__main__":
    test_connection()
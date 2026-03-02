import os
import base64
from io import BytesIO
from PIL import Image
from werkzeug.utils import secure_filename

def procesar_foto_base64(preview_base64, ruta_foto):
    if preview_base64 and ',' in preview_base64:
        try:
            encoded_data = preview_base64.split(',')[1]
            img_data = base64.b64decode(encoded_data)
            img = Image.open(BytesIO(img_data))
            img = img.convert("RGB")
            img.save(ruta_foto, format="PNG")
            return True
        except Exception as e:
            print("Error base64:", e)
            return False
    return False

def procesar_foto_archivo(foto_file, ruta_foto):
    if foto_file and foto_file.filename != '':
        filename = secure_filename(foto_file.filename)
        
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        if '.' not in filename:
            return False
        
        ext = filename.rsplit('.', 1)[1].lower()
        if ext not in allowed_extensions:
            return False
        
        try:
            img = Image.open(foto_file)
            img = img.convert("RGB")
            img.save(ruta_foto, format="PNG")
            return True
        except Exception as e:
            print("Error imagen:", e)
            return False
    return False

def crear_carpeta_si_no_existe(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
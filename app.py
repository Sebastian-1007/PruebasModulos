from flask import Flask
from config import Config  # si tienes config.py

app = Flask(__name__)
app.config.from_object(Config)

# Tus rutas aquí
@app.route('/')
def home():
    return 'Hola'

if __name__ == "__main__":
    app.run(debug=True)
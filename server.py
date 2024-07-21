from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db

# Configuración de Firebase
cred = credentials.Certificate('proyectosensoresbd-firebase-adminsdk-c4fra-5da97dd022.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyectosensoresbd-default-rtdb.firebaseio.com/'
})

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update_weight():
    data = request.get_json()
    print("Datos recibidos:", data)  # Imprime los datos recibidos para depuración
    weight = data.get('weight')

    if weight is not None:
        try:
            # Guardar el peso en Firebase
            ref = db.reference('/contenedores/1')
            ref.set({'peso': weight})
            return jsonify({"status": "success", "weight": weight}), 200
        except Exception as e:
            print("Error al guardar en Firebase:", e)  # Imprime errores en la consola
            return jsonify({"status": "error", "message": "Error al guardar en Firebase"}), 500
    else:
        return jsonify({"status": "error", "message": "No weight provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


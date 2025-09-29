from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
app = Flask(__name__)
# Establecer una clave secreta para sesiones (necesario para algunas funcionalidades de Flask), la verdad de esto nose mucho
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    info = {
        'nombre':'Rally MTB 2025',
        'organizador':'Club Social y Deportivo Unidos por el Deporte',
        'descripcion':'Carrera de MTB rural en dos modalidades: 30 km (Corta) y 80 km (Larga).',
        'fecha':'24 de Octubre de 2025',
        'fecha_iso':'2025-10-24T08:00:00',
        'horario':'08:00',
        'lugar':'Tandil, Buenos Aires',
        'tipo_carrera':'MTB rural',
        'modalidad_costo': {1:{'nombre':'Corta (30km)','valor':'10000'},2:{'nombre':'Larga (80km)','valor':'20000'}},
        'Auspiciantes':['sponsor-1.png','sponsor-2.png']
    }
    return render_template('index.html', info=info)

@app.route('/registration')
def registration():
    info = {'nombre':'Rally MTB 2025'}
    return render_template('registration.html', info=info)

@app.route('/register', methods=['POST'])
def register():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    modalidad = request.form.get('modalidad')
    print(f'Registration: {nombre} | {email} | {modalidad}')
    return jsonify({'status':'ok','message':'Inscripción recibida (simulada).'}), 200

# Se usa para que los usuarios puedan descargar archivos desde la carpeta static/docs, en este caso instalaran el deslinde de responsabilidades.
@app.route('/docs/<path:filename>')
def docs(filename):
    return send_from_directory('static/docs', filename)

if __name__ == '__main__':
    app.run(debug=True)

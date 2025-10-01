from flask import Flask, render_template, request, send_from_directory, url_for, redirect, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret' 

# Variables de entorno para el envio de mail.
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', 'False') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)


info = {
    'nombre': 'Rally MTB 2025',
    'organizador': 'Club Social y Deportivo Unidos por el Deporte',
    'descripcion': 'Carrera de MTB rural en dos modalidades: 30 km (Corta) y 80 km (Larga).',
    'fecha': '24 de Octubre de 2025',
    'fecha_iso': '2025-10-24T08:00:00',
    'horario': '08:00',
    'lugar': 'Tandil, Buenos Aires',
    'tipo_carrera': 'MTB rural',
    'modalidad_costo': {
        1: {'nombre': 'Corta (30km)', 'valor': '10000'},
        2: {'nombre': 'Larga (80km)', 'valor': '20000'}
    },
    'auspiciantes': [
        'sponsor-1.png',
        'sponsor-2.png',
        'sponsor-3.png'
    ],
    'puntos_hidratacion_30': [
        'Km 10 - RP 74',
        'Km 20 - Arroyo del Fuerte',
        'Km 30 - Paraje La Pastora'
    ],
    'puntos_hidratacion_80': [
        'Km 10 - RP 74',
        'Km 20 - Arroyo del Fuerte',
        'Km 30 - Paraje La Pastora',
        'Km 60 - Estancia El Destino'
    ],
    'kit_carrera': [
        'Remera técnica',
        'Dorsal con chip',
        'Medalla finisher',
        'Hidratación post-carrera'
    ],
    'punto_largada_llegada': 'Plaza Independencia, Tandil',
    'whatsapp_contacto': '+54 9 249 4 000000',
    'email_contacto': '6dcortez@gmail.com',
    'map_embed_src': 'https://www.google.com/maps?q=Plaza+Independencia+Tandil&output=embed'
}

@app.route('/')
def index():
    return render_template('index.html', info=info)

@app.route('/registration')
def registration():
    return render_template('registration.html', info=info)

@app.route('/register', methods=['POST'])
def register():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    dni = request.form.get('dni')
    modalidad = request.form.get('modalidad')
    comentarios = request.form.get('comentarios', '')

    try:
        body = (
            f"Inscripción recibida:\n\n"
            f"Nombre: {nombre}\n"
            f"Email: {email}\n"
            f"DNI: {dni}\n"
            f"Modalidad: {modalidad}\n"
            f"Comentarios: {comentarios}\n\n"
            f"Evento: {info['nombre']} - {info['fecha']} {info['horario']} - {info['lugar']}"
        )
        msg = Message(
            subject=f"Inscripción {info['nombre']} - {nombre}",
            recipients=[info['email_contacto']],
            body=body
        )
        mail.send(msg)
        flash('Inscripción enviada. ¡Gracias por participar!', 'success')
    except Exception as e:
        print(f"[ERROR MAIL] {e}")
        flash('No se pudo enviar el mail. Intenta nuevamente más tarde.', 'error')

    return redirect(url_for('registration'))

@app.route('/docs/<path:filename>')
def docs(filename):
    return send_from_directory('static/docs', filename)

if __name__ == '__main__':
    app.run(debug=True)

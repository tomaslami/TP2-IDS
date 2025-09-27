from flask import Flask, render_template

app = Flask(__name__)

info_evento = {
    "nombre": "Rally MTB 2025",
    "organizador": "Club Social y Deportivo Unidos por el Deporte",
    "descripcion": "Carrera de MTB rural con circuitos de 30 km y 80 km.",
    "fecha": "24 de octubre de 2025",
    "horario": "08:00",
    "lugar": "Tandil, Buenos Aires, Argentina",
    "tipo_carrera": "MTB rural",    
    "modalidades": [
        {"nombre": "Corta (30 km)", "valor": 100},
        {"nombre": "Larga (80 km)", "valor": 200},
    ],
    "kit": ["Dorsal con chip", "Medias técnicas", "Barrita energética", "Sticker del club"],
    "auspiciantes": ["Adidas", "Nike"],
    "reglamento_pdf": "reglamento.pdf",
    "deslinde_pdf": "deslinde.pdf",
}

@app.route("/")
def index():
    return render_template("index.html", evento=info_evento)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Questo endpoint riceve la parola dal frontend
@app.route("/parola", methods=["POST"])
def ricevi_parola():
    data = request.get_json()              # Legge il JSON che arriva dal frontend
    parola = data.get("parola", "")        # Prende il valore associato a "parola"
    print("Parola ricevuta:", parola)      # La stampa nei log di Render

    # Risposta che il frontend riceve
    return jsonify({
        "ok": True,
        "messaggio": "Parola ricevuta dal server Python!",
        "parola": parola
    })

# Endpoint base per testare che il server funzioni
@app.route("/")
def home():
    return "Backend Python attivo su Render"

# Avvio dell'app (Render usa la variabile d'ambiente PORT)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

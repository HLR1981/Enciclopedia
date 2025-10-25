from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

# Configuración de conexión PostgreSQL
DB_CONFIG = {
    "host": "localhost",
    "dbname": "computacion",
    "user": "postgres",
    "password": "@joseph1015",
    "port":  5432
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

@app.route("/")
def index():
    return jsonify({
        "mensaje": "API de Palabras Clave - Computación",
        "endpoints": ["/palabras", "/palabras/<id>"]
    })

@app.route("/palabras", methods=["GET"])
def get_palabras():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM palabras_clave ORDER BY porcentaje_identidad DESC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route("/palabras/<int:id>", methods=["GET"])
def get_palabra(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM palabras WHERE id = %s;", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return jsonify({"error": "Palabra no encontrada"}), 404
    return jsonify(row)

if __name__ == "__main__":
    app.run(debug=True)

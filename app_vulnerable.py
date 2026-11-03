"""
Laboratorio académico de SQL Injection con Flask y SQLite.
Ejecutar únicamente en localhost con datos ficticios.
"""
from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path(__file__).with_name("laboratorio.db")

def conectar():
    return sqlite3.connect(DB_PATH)

def inicializar_db():
    with conectar() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                clave TEXT NOT NULL
            )
        """)
        conn.execute(
            "INSERT OR IGNORE INTO usuarios (usuario, clave) VALUES (?, ?)",
            ("admin_demo", "ClaveDemo2026")
        )

@app.get("/")
def inicio():
    return jsonify({
        "proyecto": "Laboratorio SQL Injection",
        "rutas": ["/login-vulnerable", "/login-seguro"],
        "aviso": "Uso académico local. No exponer a Internet."
    })

@app.post("/login-vulnerable")
def login_vulnerable():
    datos = request.get_json(silent=True) or request.form
    usuario = str(datos.get("usuario", ""))
    clave = str(datos.get("clave", ""))

    # EJEMPLO INTENCIONALMENTE VULNERABLE: solo para demostrar el riesgo.
    consulta = (
        "SELECT id, usuario FROM usuarios "
        f"WHERE usuario = '{usuario}' AND clave = '{clave}'"
    )
    with conectar() as conn:
        resultado = conn.execute(consulta).fetchone()

    return jsonify({"autenticado": bool(resultado),
                    "mensaje": "Acceso concedido" if resultado else "Credenciales inválidas"})

@app.post("/login-seguro")
def login_seguro():
    datos = request.get_json(silent=True) or request.form
    usuario = str(datos.get("usuario", ""))
    clave = str(datos.get("clave", ""))

    # Consulta parametrizada: los datos se tratan como valores, no como SQL.
    consulta = "SELECT id, usuario FROM usuarios WHERE usuario = ? AND clave = ?"
    with conectar() as conn:
        resultado = conn.execute(consulta, (usuario, clave)).fetchone()

    return jsonify({"autenticado": bool(resultado),
                    "mensaje": "Acceso concedido" if resultado else "Credenciales inválidas"})

if __name__ == "__main__":
    inicializar_db()
    print("Laboratorio disponible solo en http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)

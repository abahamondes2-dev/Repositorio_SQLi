"""
Pruebas controladas de SQL Injection contra el laboratorio local.
No cambies TARGET para apuntar a sistemas ajenos.
"""
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

TARGET = "http://127.0.0.1:5000"

def probar(ruta, usuario, clave):
    url = TARGET + ruta
    cuerpo = json.dumps({"usuario": usuario, "clave": clave}).encode("utf-8")
    req = Request(url, data=cuerpo, headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urlopen(req, timeout=3) as respuesta:
            print(f"{ruta} | HTTP {respuesta.status} | {respuesta.read().decode('utf-8')}")
    except (URLError, HTTPError) as error:
        print(f"No se pudo completar la prueba: {error}")

if __name__ == "__main__":
    casos = [
        ("Credenciales válidas", "admin_demo", "ClaveDemo2026"),
        ("Credenciales incorrectas", "usuario_falso", "clave_falsa"),
        # Cadena de prueba inocua para comprobar el tratamiento de entradas.
        ("Entrada con caracteres SQL", "' OR '1'='1", "texto_cualquiera"),
    ]
    for nombre, usuario, clave in casos:
        print(f"\n--- {nombre} ---")
        probar("/login-vulnerable", usuario, clave)
        probar("/login-seguro", usuario, clave)

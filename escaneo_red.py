"""
Comprobación básica de puertos TCP del propio equipo (localhost).
No realiza barridos de redes ni de direcciones externas.
"""
import socket

HOST = "127.0.0.1"
PUERTOS = [22, 80, 443, 5000, 8000, 8080]

def comprobar_puerto(host, puerto, timeout=0.5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        return sock.connect_ex((host, puerto)) == 0
    finally:
        sock.close()

if __name__ == "__main__":
    print(f"Comprobación local de puertos TCP en {HOST}")
    for puerto in PUERTOS:
        estado = "ABIERTO" if comprobar_puerto(HOST, puerto) else "CERRADO"
        print(f"Puerto {puerto}: {estado}")

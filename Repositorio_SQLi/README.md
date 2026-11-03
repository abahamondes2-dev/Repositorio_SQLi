# Laboratorio académico de SQL Injection

Proyecto didáctico para observar la diferencia entre una consulta SQL construida mediante concatenación y una consulta parametrizada en una aplicación Flask con SQLite.

## Contenido

- `app_vulnerable.py`: aplicación Flask con dos rutas de demostración: una vulnerable y otra protegida.
- `ataque_sql_i.py`: ejecuta casos de prueba únicamente contra `127.0.0.1`.
- `escaneo_red.py`: comprueba puertos TCP seleccionados del propio equipo.
- `MANUAL_USO.md`: instrucciones de instalación y ejecución.
- `requirements.txt`: dependencia de Flask.
- `evidencias/`: espacio para agregar capturas reales de la ejecución.

## Requisitos

- Python 3.10 o superior.
- pip.
- Navegador web o terminal.

## Inicio rápido

Consulta `MANUAL_USO.md` para instalar dependencias, iniciar el servidor y ejecutar las pruebas.

## Alcance y uso responsable

Este repositorio está diseñado para un laboratorio local con información ficticia. El servidor escucha exclusivamente en `127.0.0.1`; no lo publiques en Internet ni uses los scripts contra sistemas de terceros. La ruta vulnerable existe solo para fines demostrativos.

## Resultado esperado

Con las credenciales de demostración, ambas rutas deben autenticar al usuario ficticio. Las pruebas con entradas manipuladas permiten comparar el comportamiento de la ruta vulnerable con el de la ruta protegida. El comportamiento exacto debe verificarse en la ejecución local y documentarse con capturas propias.

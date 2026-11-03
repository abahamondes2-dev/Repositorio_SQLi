# Manual de instalación y uso

## 1. Preparar el entorno

Instala Python 3.10 o superior. Descarga o clona el repositorio y abre una terminal dentro de la carpeta `Repositorio_SQLi`.

## 2. Crear un entorno virtual

En Windows:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, puedes usar:

```cmd
.venv\Scripts\activate.bat
```

En Linux o macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Iniciar la aplicación

```bash
python app_vulnerable.py
```

En la terminal debe aparecer que el laboratorio está disponible en `http://127.0.0.1:5000`. Mantén esa terminal abierta.

## 5. Ejecutar las pruebas de SQL Injection

Abre una segunda terminal en la carpeta del proyecto, activa el mismo entorno virtual y ejecuta:

```bash
python ataque_sql_i.py
```

El programa compara tres casos de entrada en las rutas `/login-vulnerable` y `/login-seguro`. Las pruebas se envían exclusivamente al servidor local.

Credenciales ficticias para la prueba válida:

- Usuario: `admin_demo`
- Clave: `ClaveDemo2026`

## 6. Comprobar puertos locales

En otra terminal, ejecuta:

```bash
python escaneo_red.py
```

El script revisa únicamente los puertos definidos en `127.0.0.1`. El puerto 5000 debería aparecer abierto mientras Flask esté ejecutándose.

## 7. Evidencias para el informe

Toma capturas reales de:

1. La terminal con Flask iniciado.
2. La ejecución de `ataque_sql_i.py` y sus resultados.
3. La ejecución de `escaneo_red.py`.
4. El código de la consulta parametrizada en `app_vulnerable.py`.

Guarda las imágenes en la carpeta `evidencias/` y usa nombres descriptivos. No presentes capturas simuladas como si fueran resultados reales.

## 8. Detener y limpiar

Presiona `Ctrl + C` en la terminal del servidor. Para salir del entorno virtual:

```bash
deactivate
```

La base `laboratorio.db` se crea automáticamente al iniciar la aplicación. Puedes eliminarla cuando el servidor esté detenido para reiniciar los datos ficticios.

## 9. Limitaciones y seguridad

Este proyecto es un entorno educativo local. No cambies el destino de los scripts ni ejecutes pruebas contra páginas, redes o servicios que no sean tuyos y para los que no tengas autorización expresa. La ruta vulnerable no debe desplegarse en producción.

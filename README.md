# Enciclopedia
# Proyecto: Palabras Clave - Computación

Este proyecto crea una base de datos en PostgreSQL con palabras clave del tema "Computación"
y expone una API Flask que devuelve los datos en formato JSON.

## Archivos
- app.py → Servidor Flask (ejecutable principal)
- palabras.sql → Script SQL de la tabla
- requirements.txt → Dependencias
- README.md → Instrucciones de uso

# Ejecución

1. Crea la base de datos:
   createdb palabras_clave_db
   psql -d palabras_clave_db -f palabras.sql

2. Instala dependencias:
   pip install -r requirements.txt

3. Ejecuta la aplicación:
   python app.py

4. Abre en el navegador:
   http://127.0.0.1:5000/palabras
# Proyecto: Palabras Clave - Computación

Este proyecto crea una base de datos en PostgreSQL con palabras clave del tema "Computación"
y expone una API Flask que devuelve los datos en formato JSON.

## Archivos
- app.py → Servidor Flask (ejecutable principal)
- palabras.sql → Script SQL de la tabla
- requirements.txt → Dependencias
- README.md → Instrucciones de uso

## Ejecución
1. Crea la base de datos:
   createdb palabras_clave_db
   psql -d palabras_clave_db -f palabras.sql

2. Instala dependencias:
   pip install -r requirements.txt

3. Ejecuta la aplicación:
   python app.py

4. Abre en el navegador:
   http://127.0.0.1:5000/palabras

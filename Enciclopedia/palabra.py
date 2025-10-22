import psycopg2

# Datos de conexión a la base de datos PostgreSQL
DB_NAME = "computación"
DB_USER = "postgres"
DB_PASSWORD = "@joseph1015"
DB_HOST = "localhost"
DB_PORT = "5432"

# Lista de palabras clave relacionadas con computación
palabras_clave = [
    ('Algoritmo', 95.00, 'procedimiento, método'),
    ('Programación', 98.00, 'codificación, desarrollo de software'),
    ('Hardware', 90.00, 'equipo, componentes físicos'),
    ('Software', 95.00, 'programas, aplicaciones'),
    ('Base de datos', 92.00, 'repositorio, almacenamiento de datos'),
    ('Redes', 88.00, 'conectividad, telecomunicaciones'),
    ('Inteligencia Artificial', 96.00, 'IA, aprendizaje automático'),
    ('Sistema Operativo', 93.00, 'OS, plataforma'),
    ('Lenguaje de programación', 97.00, 'Java, Python, C++'),
    ('Computadora', 94.00, 'ordenador, PC'),
    ('Seguridad informática', 91.00, 'ciberseguridad, protección de datos'),
    ('Algoritmo de búsqueda', 89.00, 'exploración, localización'),
    ('Interfaz gráfica', 87.00, 'GUI, entorno visual'),
    ('Compilador', 90.00, 'traductor, intérprete'),
    ('Arquitectura de computadoras', 92.00, 'estructura, diseño de sistemas')
]

# Conexión a PostgreSQL y creación de tabla
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()

    # Crear tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS palabras_clave (
            palabra TEXT PRIMARY KEY,
            porcentaje_identidad DECIMAL(5,2),
            sinonimos TEXT
        );
    """)

    # Insertar datos
    cursor.executemany("""
        INSERT INTO palabras_clave (palabra, porcentaje_identidad, sinonimos)
        VALUES (%s, %s, %s)
        ON CONFLICT (palabra) DO NOTHING;
    """, palabras_clave)

    conn.commit()

    # Mostrar datos insertados
    cursor.execute("SELECT * FROM palabras_clave;")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)

    cursor.close()
    conn.close()

except Exception as e:
    print("Error al conectar o ejecutar en la base de datos:", e)
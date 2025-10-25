CREATE TABLE IF NOT EXISTS palabras (
    id SERIAL PRIMARY KEY,
    palabra TEXT NOT NULL,
    porcentaje_identity NUMERIC(5,2) NOT NULL CHECK (porcentaje_identity >= 0 AND porcentaje_identity <= 100),
    sinonimos TEXT[]
);

INSERT INTO palabras (palabra, porcentaje_identity, sinonimos) VALUES
('Algoritmo', 98.00, ARRAY['procedimiento','método','proceso']),
('Programación', 100.00, ARRAY['codificación','desarrollo','scripting']),
('Hardware', 85.00, ARRAY['componentes físicos','dispositivos','equipo']),
('Software', 95.00, ARRAY['programas','aplicaciones','sistemas']),
('Base de datos', 92.00, ARRAY['almacenamiento de datos','DBMS']),
('Redes', 88.00, ARRAY['networking','comunicación']),
('Inteligencia Artificial', 93.00, ARRAY['IA','machine intelligence']),
('Machine Learning', 91.00, ARRAY['aprendizaje automático','ML']),
('Big Data', 84.00, ARRAY['datos masivos','analítica']),
('Ciberseguridad', 89.00, ARRAY['seguridad informática','protección de datos']),
('Computación en la Nube', 87.00, ARRAY['cloud computing','nube']),
('Virtualización', 80.00, ARRAY['máquinas virtuales','VM']),
('Lenguajes de Programación', 96.00, ARRAY['Python','Java','C++']),
('Criptografía', 82.00, ARRAY['encriptación','cifrado']),
('Minería de Datos', 83.00, ARRAY['data mining','extracción de patrones']);

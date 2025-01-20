# SQL Insert Formatter

Una herramienta simple pero poderosa que formatea sentencias SQL INSERT de múltiples líneas a una sola línea, manteniendo la integridad de los datos y facilitando su procesamiento.

## 🚀 Características

- Convierte INSERTs de múltiples líneas a una sola línea
- Preserva la integridad de los datos
- Soporta caracteres especiales y codificación UTF-8
- Usa Docker para fácil implementación
- No requiere dependencias externas
- Mantiene los comentarios SQL

## 📋 Ejemplo

### Entrada (inserts.sql):
```sql
INSERT INTO estudiantes 
    (rut_estudiante, nombre_estudiante, fecha_nacimiento, 
    direccion, correo, telefono)
VALUES 
    ('11111111-1', 'nombre_estudiante_1', '1990-08-27', 
    'dirección 1', 'estudiante_1@mail.com', '123456677889');
```

### Salida (inserts_formateados.sql):
```sql
INSERT INTO estudiantes (rut_estudiante, nombre_estudiante, fecha_nacimiento, direccion, correo, telefono) VALUES ('11111111-1', 'nombre_estudiante_1', '1990-08-27', 'dirección 1', 'estudiante_1@mail.com', '123456677889');
```

## 🛠️ Instalación y Uso

1. Clona el repositorio:
```bash
git clone [URL_del_repositorio]
cd sql-insert-formatter
```

2. Asegúrate de tener los siguientes archivos en tu directorio:
```
proyecto/
├── docker-compose.yml
├── main.py
└── inserts.sql        # Tu archivo con los INSERTs
```

3. Ejecuta el contenedor:
```bash
docker-compose up
```

4. El resultado se guardará en `inserts_formateados.sql`

## 📝 Notas Importantes

- El archivo de entrada debe llamarse `inserts.sql` o asignar un nombre de forma explicita dentro del codigo de main.py en la linea 5
- El archivo debe estar en la misma carpeta que el `docker-compose.yml`
- El resultado se generará como `import.sql`
- La herramienta mantiene los comentarios SQL (líneas que comienzan con --)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo LICENSE para detalles

## ✨ Ejemplo con Comentarios

### Entrada:
```sql
-- Insert estudiantes
INSERT INTO estudiantes 
    (rut_estudiante, nombre_estudiante) 
VALUES 
    ('11111111-1', 'nombre_1');

-- Insert cursos
INSERT INTO cursos 
    (codigo_curso, nombre_curso) 
VALUES 
    ('001', 'Python Básico');
```

### Salida:
```sql
-- Insert estudiantes
INSERT INTO estudiantes (rut_estudiante, nombre_estudiante) VALUES ('11111111-1', 'nombre_1');
-- Insert cursos
INSERT INTO cursos (codigo_curso, nombre_curso) VALUES ('001', 'Python Básico');
```

## ⚠️ Consideraciones

- Asegúrate de tener Docker instalado en tu sistema
- El archivo de entrada debe tener codificación UTF-8
- Cada sentencia INSERT debe terminar con punto y coma (;)
- Los comentarios SQL se mantendrán en el archivo de salida
```

¿Te gustaría que añada o modifique alguna sección del README?
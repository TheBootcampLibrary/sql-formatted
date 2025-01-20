import os

def format_sql_inserts():
    # Definimos los nombres de archivos en la raíz del proyecto
    input_file = "inserts.sql"  # Archivo original
    output_file = "import.sql"  # Archivo resultante
    
    # Verificamos que el archivo de entrada existe
    if not os.path.exists(input_file):
        print(f"Error: El archivo {input_file} no existe en la raíz del proyecto")
        return
    
    # Variable para almacenar la línea actual que estamos construyendo
    current_line = ""
    
    try:
        # Abrimos el archivo de entrada para lectura y el de salida para escritura
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            
            for line in infile:
                # Eliminamos espacios en blanco al inicio y final
                line = line.strip()
                
                if line:  # Si la línea no está vacía
                    # Agregamos la línea actual a nuestra construcción
                    current_line += " " + line
                    
                    # Si encontramos un punto y coma, es el final de la sentencia
                    if line.endswith(';'):
                        # Limpiamos espacios múltiples y escribimos al archivo
                        cleaned_line = ' '.join(current_line.split())
                        outfile.write(cleaned_line + '\n')
                        # Reseteamos la línea actual
                        current_line = ""
        
        print(f"Proceso completado. El archivo resultante es: {output_file}")
        
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

# Ejecutamos la función cuando se corre el script
if __name__ == "__main__":
    format_sql_inserts()
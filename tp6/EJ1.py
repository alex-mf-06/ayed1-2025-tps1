import os
from typing import List

def cargar_lineas_txt(ruta_archivo: str) -> List[str]:
    """
    Carga las líneas desde un archivo de texto (.txt) de forma segura.
    - Si el archivo existe, devuelve una lista con sus líneas.
    - Si el archivo NO existe, lo crea vacío y devuelve una lista vacía [].
    """
    try:
        # Intenta abrir y leer el archivo en modo lectura ('r').
        with open(ruta_archivo, 'rt', encoding='utf-8') as file:
            # Lee todas las líneas, quita espacios/saltos de línea y las devuelve en una lista.
            return [line.strip() for line in file] #list comprehension para limpiar líneas

    except FileNotFoundError:
        # Si el archivo no existe, esta sección se ejecuta.
        print(f"Advertencia: El archivo '{ruta_archivo}' no se encontró. Se creará uno nuevo.")
        try:
            # Aseguramos que el directorio exista antes de crear el archivo.
            directorio = os.path.dirname(ruta_archivo)
            if directorio: # Solo crear si la ruta tiene un directorio
                os.makedirs(directorio, exist_ok=True)
            
            # Creamos el archivo de texto vacío.
            with open(ruta_archivo, 'wt', encoding='utf-8') as file:
                pass # Simplemente crea el archivo
            
            # Devolvemos una lista vacía, que es el contenido del archivo recién creado.
            return []
            
        except Exception as e:
            # Si hay un error al intentar crear el archivo (ej: permisos).
            print(f"Error crítico: No se pudo crear el archivo '{ruta_archivo}'. Motivo: {e}")
            return []
        
    except Exception as e:
        # Captura cualquier otro error inesperado.
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        return []

def guardar_Nombres_segun_nacionalidad() -> None:
    """
    Guarda Los nombres en archivos según su nacionalidad. si su apellido terminaba en IAN se guardaba en armenia.txt , si terminaba en INI se guardaba en italia.txt , si el apellido terminaba en EZ se guardaba en españa.txt y si no cumplia con ninguna de esas condiciones no se guardaba en ningun archivo.
    """
    try:
        ruta_nombres = os.path.join("datos","informacion_nombres.txt")
        nombres = cargar_lineas_txt(ruta_nombres)
        archivo_armenia = os.path.join("datos","ARMENIA.txt")
        archivo_italia = os.path.join("datos","ITALIA.txt")
        archivo_espana = os.path.join("datos","ESPAÑA.txt")
        
        with open(archivo_armenia, 'wt', encoding='utf-8') as armenia_file,\
             open(archivo_italia, 'wt', encoding='utf-8') as italia_file, \
             open(archivo_espana, 'wt', encoding='utf-8') as espana_file:

            for nombre in nombres:
                apellido = nombre.strip().split()[0].upper()  # Obtener el apellido y convertir a mayúsculas
                if not apellido:
                    continue  # Saltar si la línea está vacía
                
                elif apellido.endswith('IAN'): # Apellido armenio
                    armenia_file.write(nombre + '\n') # Escribir el nombre completo en el archivo de Armenia

                elif apellido.endswith('INI'): # Apellido italiano
                    italia_file.write(nombre + '\n') # Escribir el nombre completo en el archivo de Italia

                elif apellido.endswith('EZ'): # Apellido español
                    espana_file.write(nombre + '\n') # Escribir el nombre completo en el archivo de España
    except Exception as e:
        print(f"Error al guardar nombres según nacionalidad: {e}")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
if __name__ == "__main__":
    guardar_Nombres_segun_nacionalidad()
import os

def dividir_archivo_por_tamaño_corregido() -> None:
    """
    Divide un archivo de texto en varios archivos más pequeños según un tamaño máximo 
    especificado y agrega un sufijo numérico a cada archivo dividido.
    Lee el archivo de entrada línea por línea sin cargarlo completo en memoria.

    precondicion: El archivo de texto debe existir en la ruta especificada por el usuario.
    postcondicion: Se crean varios archivos de texto en la misma ubicación que el archivo 
                   original, cada uno con un tamaño máximo especificado.
    """
    try:
        ruta_archivo = input("Ingrese la ruta del archivo de texto a dividir: ").strip()
        # Mantenemos tu estructura de unirse a la carpeta "datos"
        ruta_archivo = os.path.join("datos", ruta_archivo)

        # --- CORRECCIÓN 1: Verificar existencia antes de leer ---
        if not os.path.exists(ruta_archivo):
            print(f"Error: El archivo '{ruta_archivo}' no existe.")
            return

        tamaño_maximo = int(input("Ingrese el tamaño máximo para cada archivo dividido (kbytes): ").strip())
        if tamaño_maximo <= 0:
            print("El tamaño máximo debe ser un número positivo.")
            return
        
        tamaño_maximo_bytes = tamaño_maximo * 1024  # Convertir a bytes

        archivos_creados = 1  
        bytes_acumulados = 0
        
        base_nombre, extension = os.path.splitext(ruta_archivo) # Obtener el nombre base y la extensión ejemplo : ("archivo"," .txt")
        
        ruta_parte_actual = f"{base_nombre}_parte{archivos_creados}.txt"

        with open(ruta_archivo, 'r', encoding='utf-8') as f_in:
            
            for linea in f_in: # Leer línea por línea 
               
                tamano_linea = len(linea.encode('utf-8')) # Obtener el tamaño en bytes de la línea actual
                
               
                if tamano_linea > tamaño_maximo_bytes: # si la línea es más grande que el tamaño máximo
                    print(f"Error: Una línea ({tamano_linea} bytes) es más grande que el tamaño máximo permitido ({tamaño_maximo_bytes} bytes).")
                    print("Proceso cancelado.")
                    

                
                if (bytes_acumulados + tamano_linea > tamaño_maximo_bytes) and (bytes_acumulados > 0): # si se excede el tamaño máximo
                    
                    archivos_creados += 1
                    bytes_acumulados = 0  # Reiniciar el contador de bytes
                    # Actualizar el nombre del archivo de salida
                    ruta_parte_actual = f"{base_nombre}_parte{archivos_creados}.txt"

                # Escribir la línea en el archivo de parte actual (sea el viejo o el nuevo)
                with open(ruta_parte_actual, 'a', encoding='utf-8') as nuevo_archivo:
                    nuevo_archivo.write(linea) # 'linea' ya incluye el '\n'
                    bytes_acumulados += tamano_linea # Actualizar el contador de bytes

        print(f"Proceso completado. Total de archivos creados: {archivos_creados}")

    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
    except ValueError:
        print("Error: El tamaño máximo debe ser un número entero válido.")
    except FileNotFoundError: # Captura si 'os.path.join' falla o la carpeta no existe
         print(f"Error: No se pudo encontrar la ruta o el archivo: {ruta_archivo}")
    except Exception as e:
        print(f"Error inesperado al dividir el archivo: {e}")

# --- Ejecutar la función corregida ---
if __name__ == "__main__":
    dividir_archivo_por_tamaño_corregido()
    
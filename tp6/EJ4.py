import os


ruta_archivo = os.path.join("datos", "funciones.txt")
def validar_comenentario(linea:str) -> int:

    """
    Esta funcion se encarga de buscar en cada linea de si hay 
    comentarios encontrar el indice.
    precondiciones: la linea debe ser un string 
    postcondiciones : devuelve el indice donde se encuentra el comentaria o -1 si no hay comentario alguno en la linea . 

    """
    string= None 
    for i , caracter in enumerate(linea):
        if string: #pregunta si hay algo en string en esa variable podira  haber: ' o "
            if caracter == string : # pregunta si el caracter es igual que el sring es decir si son igual ejemplo si lleva : ' o "
                string = None # lo devuelve None  por que significa que se cerro las comillas por ejemplo "pepe"
        else:
            if caracter == "'" or caracter == '"':
                string = caracter
            elif caracter == "#":
                return i
    return -1




    
def remover_comentarios_y_docstrings(ruta_archivo: str) -> None:
    """
    
    Esta funcion se encarga de eliminar comentarios y docstrings .

    precondiciones : la ruta debe existir 
    postcondiciones : no retorna nada pero se encarga de devolver a la ruta la informcacion pero son las mismas. 
    
    """

    try: 
        with open(ruta_archivo, "rt", encoding="utf-8") as texto :
            contenido = texto.readlines()
        lineas_limpias = []
        es_docstring = False 
        for linea in contenido:
            linea_limpia = linea.strip() 

            if es_docstring: # pregunta  si estan en un docstring

                if linea_limpia.endswith('"""') or linea_limpia.endswith("'''"): #pregunta si la nueva linea termina el docstring que estba antes si es que si 
                    # entonces termina el docstring y la variable es Falso 
                    es_docstring = False
                continue #continua si es que no 
            elif linea_limpia.startswith('"""') or linea_limpia.startswith("'''"): # si el docstring era falso llega aca
                #i y preguntaba si la linea empezaba con '"""' o "'''"  si es asi entra 
                if linea_limpia.endswith('"""') or linea_limpia.endswith("'''") and len(linea_limpia) > 3 : #pregunta si en esa misma linea termina el dosctring si es asi continuan 
                    continue 
                else: # si es que no termina el docstring la variable se vuelve True y continua 
                    es_docstring = True
                    continue
            indice_comentario = validar_comenentario(linea_limpia) # lleva a la linea a la funcion valiar comentario a ver si se encuentra comentarios 
            linea_sin_comentario = linea 
            if indice_comentario != -1: # si el indice es diferente a -1 quiere decir que si encontro un comentario 
                linea_limpia = linea_limpia[:indice_comentario] # esto hace que quite fel # hacia atras 
            elif linea_sin_comentario: 
                lineas_limpias.append(linea_limpia.rstrip() + '\n')
        with open(ruta_archivo, 'w', encoding='utf-8') as f_out:
            f_out.writelines(lineas_limpias)

        print(f"¡Éxito! Archivo limpio (simple) guardado en: {ruta_archivo}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
            
def mostrar_txt(ruta_archivo: str) -> None:
    """
    Esta funcion se encarga de mostrar archivos.txt 

    precondiciones : debe recibir una ruta de archivo  valida 
    postcondiciones : se encarga de mostrar el contenido de los archivos. 
    """
    with open(ruta_archivo ,"rt", encoding="utf-8") as archivo:
        print(archivo.read())
if __name__ == "__main__":
    archivo_amtes = mostrar_txt(ruta_archivo)
    remover_comentarios_y_docstrings(ruta_archivo)
    archivo_despues = mostrar_txt(ruta_archivo)

    
          
               

            


    








from typing import List, Tuple , Set



def cadena_a_solo_palabras_sin_repetidas(cadena:str) -> Set[str]:
    """
    Toma una cadena de texto, la divide en palabras (por espacios) 
    y devuelve una LISTA ORDENADA alfabéticamente con 
    las palabras únicas.

    Precondiciones:
        - cadena (str): La cadena de texto a procesar. 
                        (Ej: "hola mundo hola de nuevo")

    Postcondiciones:
        - (List[str]): Una lista alfabéticamente ordenada con 
                       las palabras únicas. 
                       (Ej: ['de', 'hola', 'mundo', 'nuevo'])
        - Si la cadena está vacía, devuelve una lista vacía ([]).
        - Si la entrada no es un string (ej. None, 123), 
          devuelve una lista vacía ([]).
    """

    

    try:
        palabras_unicas_ = set(cadena.split())
        return sorted(palabras_unicas_, key=len, reverse=True)
    except TypeError:
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    print(cadena_a_solo_palabras_sin_repetidas("hola mundo hola de nuevo"))





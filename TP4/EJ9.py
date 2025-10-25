def ordenar_xLongitud(cadena: str) -> str:
    """
    Ordena las palabras de una cadena de texto según su longitud, de menor a mayor.
    
    Precondiciones:
    - El parámetro 'cadena' debe ser un string.
    
    Postcondiciones:
    - Devuelve un nuevo string con las palabras de la cadena original ordenadas por su longitud.
    - Lanza TypeError si el parámetro 'cadena' no es un string.
    """
    try:
        palabras = cadena.split()
    except AttributeError:
        raise TypeError("El parámetro 'cadena' debe ser un string.")

    palabras_ordenadas = sorted(palabras, key=len)
    return " ".join(palabras_ordenadas)



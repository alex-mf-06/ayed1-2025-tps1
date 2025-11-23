
def convertir_bin_a_decimales(numero_binario: str) -> int:
    """
    Convierte un número binario (en formato de cadena) a su equivalente en base decimal.

    Precondiciones:
    - numero_binario (str): Una cadena que representa un número binario válido 
                            (solo contiene '0' y '1').

    Postcondiciones:
    - (int): El número decimal equivalente.
    - Devuelve 0 si la cadena no es un número binario válido o si ocurre un error.
    """
    try:
        # La función int() con el segundo argumento como 2 convierte una cadena binaria a decimal.
        return int(numero_binario, 2)
    except (ValueError, TypeError):
        # Si la cadena contiene caracteres no válidos ('0' o '1') o no es una cadena,
        # int() lanzará un ValueError o TypeError.
        return 0
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return 0


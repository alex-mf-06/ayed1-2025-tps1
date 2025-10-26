def sum_cadenas_y_devolver_numero(cadena1:str,cadena2:str) ->float:
    """Recibe dos cadenas que representan números reales, las convierte a float, las suma y retorna el resultado como un entero.
    precondiciones: cadena1 y cadena2 deben ser cadenas que representen números reales válidos.
    postcondiciones:
    - Retorna la suma de los dos números como un float.
    """
    try:
        numero1 = float(cadena1)
        numero2 = float(cadena2)
        suma = numero1 + numero2
        return suma
    except ValueError:
        return -1
    except TypeError:
        return -1
if __name__ == "__main__":
    assert sum_cadenas_y_devolver_numero("3.5", "2.5") == 6.0
    assert sum_cadenas_y_devolver_numero("10", "20.5") == 30.5
    assert sum_cadenas_y_devolver_numero("abc", "2.5") == -1
    assert sum_cadenas_y_devolver_numero("3.5", "xyz") == -1
    assert sum_cadenas_y_devolver_numero("abc", "xyz") == -1



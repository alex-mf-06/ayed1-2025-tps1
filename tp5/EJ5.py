def raiz_cuadrada(n: int) -> float|None:
    """
    Calcula la raíz cuadrada de un número entero positivo.
    precondiciones: n debe ser un número entero positivo.
    postcondiciones: devuelve la raíz cuadrada de n en formato float.
    """
    try:
        n = int(n)
        if n < 0:
            return None
        return n ** 0.5
    except ValueError :
        return None
    except TypeError:
        return None

if __name__ == "__main__":
    assert raiz_cuadrada(9) == 3.0
    assert raiz_cuadrada(0) == 0.0
    assert raiz_cuadrada(16) == 4.0
    assert raiz_cuadrada(-4) == None
    assert raiz_cuadrada("a") == None
    assert raiz_cuadrada([12,3]) == None
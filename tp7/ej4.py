
def multiplicar(numero1:int, numero2:int)->int:
    """Función que recibe dos números enteros y devuelve su producto.

    Args:
        numero1 (int): Primer número entero.
        numero2 (int): Segundo número entero.

    Returns:
        int: Producto de los dos números enteros.
    """
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        if numero2 == 1:
            return numero1
        else:
            return numero1 + multiplicar(numero1, numero2 - 1)
    except TypeError:
        return 0
    except ValueError:
        return 0
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return 0
if __name__ == "__main__":
    print(multiplicar(5,3))
    assert multiplicar(5, 3) == 15
    assert multiplicar(0, 10) == 0
    assert multiplicar(-2, 4) == -8







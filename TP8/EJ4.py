
from typing import Tuple

def crear_ficha() -> Tuple[int, int]:
    """
    
    
    """
    try:
        ficha = []
        while True:
            try:
                mitad_ficha = input("INgrese el numero de la mitad de la ficha : ").strip()
                if mitad_ficha.isdigit():
                    mitad_ficha = int(mitad_ficha)
                    if mitad_ficha >= 0 and mitad_ficha <= 6:
                        ficha.append(mitad_ficha)
                        if len(ficha) == 2:
                            return tuple(ficha)
                    else:
                        print("El número debe estar entre 0 y 6.")
                else:
                    print("El número debe ser un número entero.")
            except KeyboardInterrupt:
                print("Solo vas a salir si ingresas una ficha valida")
                continue


    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    
def encajan(ficha1: Tuple[int, int], ficha2: Tuple[int, int]) -> bool:
    """
    Indica si dos fichas de dominó encajan.
    
    PRECONDICIONES:
    - Cada ficha es una tupla de dos enteros entre 0 y 6.
      Ej: (3,4)

    POSTCONDICIONES:
    - Devuelve True si comparten algún número, False si no.

    EJEMPLO:
    (3,4) y (5,4) → True
    (2,6) y (1,3) → False
    """

    return not set(ficha1).isdisjoint(set(ficha2))


# Programa para probar la función
if __name__ == "__main__":

    primer_ficha = crear_ficha()
    segunda_ficha = crear_ficha()
    print(encajan(primer_ficha, segunda_ficha))
    






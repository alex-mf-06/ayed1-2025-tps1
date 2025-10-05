from typing import List
import random
def impares(cantidad:int) -> tuple[int]:
    """
    Genera una lista de números impares a partir de una lista de números aleatorios.
    precondición: cantidad debe ser un entero positivo.
    postcondición: devuelve una lista de números impares generados aleatoriamente.
    """
    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError("Error: 'cantidad' debe ser un entero positivo.")
    except ValueError:
        print("Error: 'cantidad' debe ser un número entero válido.")
        return -1
    except TypeError:
        print("Error: La entrada o la salida no es un número entero válido.")
        return -1
    lista_random = [random.randint(1,100) for x in range(cantidad)]
    impares = list(filter(lambda x : x % 2 != 0 , lista_random))
    return lista_random, impares
cantidad = 20

if __name__ == "__main__":
    lista_random, lista_impares = impares(cantidad)
    print(f"Lista de números aleatorios: {lista_random}")
    print(f"Lista de números impares: {lista_impares}")
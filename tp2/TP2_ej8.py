from typing import List
#ejercicio 8    
def impares(inicio:int, fin:int) -> List[int]:
    """
    Genera una lista de números impares en un rango dado entre inicio y fin.
    precondición: inicio y fin deben ser enteros donde inicio es menor que fin.
    postcondición: devuelve una lista de números impares entre inicio y fin (inclusive).
    """
    try:
        inicio = int(inicio)
        fin = int(fin)
        if inicio >= fin:
            raise ValueError("Error: 'inicio' debe ser menor que 'fin'.")
    except ValueError:
        print("Error: 'inicio' y 'fin' deben ser números enteros válidos.")
        return -1
    except TypeError:
        print("Error: La entrada o la salida no es un número entero válido.")
        return -1
    return [i for i in range(inicio, fin + 1) if i % 2 != 0]

impares_lista = impares(100, 200)
print(impares_lista)  # Muestra la lista de números impares entre 100 y 
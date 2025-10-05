from typing import List

#ejercicio 6 

def normalizar(lista: List[int]) -> List[float]:
    """
    Normaliza los valores de una lista de números enteros a una escala de 0 a 1.
    Contrato: La lista no debe estar vacía.
    precondición: La lista no debe estar vacía y debe ser una lista de enteros.
    postcondición: Devuelve una lista de números flotantes normalizados.

    """
    try : 
        listaa= [x / sum(lista) for x in lista] # Normaliza los valores a una escala de 0 a 1
        if not lista:
            raise ValueError("La lista no debe estar vacía.")
    except TypeError:
        raise TypeError("Error: La entrada no es una lista válida o directamente no es una lista .")
    return listaa

print(normalizar([1,2,2]))
assert normalizar([1,2,2]) == [0.2, 0.4, 0.4] # Normaliza a [0.2, 0.4, 0.4]
assert normalizar([9,9,9,13]) == [0.225, 0.225, 0.225, 0.325] #aproximado

from typing import List
#ejercicio 7 
def intercalando(lista1: List[int], lista2: List[int]) -> List[int]:
    """
    Intercala dos listas de números enteros y las vuelve en una nueva lista(se añade a la lista 1 -__-) con todos los elementos de las 2 anteriores listas.
    precondición: ambas listas no están vacías y deben ser listas de enteros.
    postcondición: devuelve una nueva lista con los elementos de ambas listas intercalados.

    """
    try:
       
        _ = sum(lista1) + sum(lista2)

      
        for i, v in enumerate(lista2):
            indice = i * 2 + 1
            lista1[indice:indice] = [v]
        return lista1

    except TypeError:
        raise TypeError("Error: ambas entradas deben ser listas con números enteros.")
    except Exception as e:
        raise Exception(f"Ocurrió un error inesperado: {e}")
print(intercalando([1,3,5],[2,4,6])) # [1,2,3,4,5,6]
print(intercalando([10,20,30],[15,25,35])) # [10,15,20,25,30,35]
assert intercalando([1,3,5],[2,4,6]) == [1,2,3,4,5,6]
assert intercalando([10,20,30],[15,25,35]) == [10,15,20,25,30,35]
assert intercalando([1,2,3],[4,5,6]) != [1,4,2,5,3,2]

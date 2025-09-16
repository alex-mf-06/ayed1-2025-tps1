#ejercicio 7 
def intercalando(lista1: list[int], lista2: list[int]) -> list[int]:
    """
    Intercala dos listas de números enteros y las vuelve en una nueva lista(se añade a la lista 1 -__-) con todos los elementos de las 2 anteriores listas.

    """
    for i,v in enumerate(lista2): # Itera sobre los elementos de la segunda lista
        indice = i * 2 + 1 # Calcula el índice de inserción
        lista1[indice:indice] = [v] # Inserta el elemento de la segunda lista en la posición calculada
    return lista1

print(intercalando([1,3,5],[2,4,6])) # [1,2,3,4,5,6]

assert intercalando([1,3,5],[2,4,6]) == [1,2,3,4,5,6]
assert intercalando([10,20,30],[15,25,35]) == [10,15,20,25,30,35]
assert intercalando([1,2,3],[4,5,6]) != [1,4,2,5,3,2]

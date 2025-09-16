#ejercicio 8    
def impares(inicio:int, fin:int) -> list[int]:
    """
    Genera una lista de números impares en un rango dado entre inicio y fin.
    """
    return [i for i in range(inicio, fin + 1) if i % 2 != 0]

impares_lista = impares(100, 200)
print(impares_lista)  # Muestra la lista de números impares entre 100 y 
from typing import List
def multiplo_7_no_de_5(inicio:int , fin:int)-> List[int]:
    """
    Genera una lista de números que son múltiplos de 7 pero no de 5 en un rango dado
    precondición: inicio y fin deben ser enteros donde inicio es menor que fin.
    postcondición: devuelve una lista de números que son múltiplos de 7 pero no de 5 entre inicio y fin (inclusive).
    """
    try:
        inicio = int(inicio)
        fin = int(fin)
        if inicio >= fin:
            raise ValueError("Error: 'inicio' debe ser menor que 'fin'.")
    except ValueError:
        print("Error: 'inicio' y 'fin' deben ser números enteros válidos.")
        return -1
    return [i for i in range(inicio, fin + 1) if i % 7 == 0 and i % 5 != 0]
print(multiplo_7_no_de_5(1, "100"))

#ejercicio 10
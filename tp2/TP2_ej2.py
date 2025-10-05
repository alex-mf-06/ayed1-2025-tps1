import random as rd
from typing import List
#ejercicio 2 tp2
guion = lambda x: "-" * x
def cargar_lista(cantidad:int)-> List[List[int]]:
    """
    Carga una lista de listas con números enteros aleatorios.

    """
    try:
        cantidad = int(cantidad)
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        return None
    except TypeError:
        print("Error: La entrada no es un número entero válido.")
        return None
    
    if cantidad < 1:
        raise ValueError("La cantidad debe ser un entero positivo.")
    lista = [rd.randint(1,100) for _ in range(cantidad)]
    return lista

def hay_repetidos(lista:List[int]) -> bool:
    """
    Verifica si hay elementos repetidos en la lista va a devolver True si hay repetidos y False si no.
    precondición: la lista no está vacía y debe ser una lista de enteros.
    postcondición: devuelve True si hay elementos repetidos, False en caso contrario.
    """
    for i in range(len(lista)):
        elem= lista[i]
        for elemento in lista[i+1:]:
            if elem == elemento:
                return True
    return False
def eliminar_repetidos(lista:List[int]) -> List[int]:
    """
    Elimina los elementos repetidos de la lista y devuelve una nueva lista sin duplicados.
    precondición: la lista no está vacía y debe ser una lista de enteros.
    postcondición: devuelve una lista sin elementos repetidos.
    """
    try:
        if len(lista) == 0:
            raise ValueError("La lista está vacía.")
    except TypeError:
        print("Error: La entrada no es una lista válida.")
        return None
    
    set_sin_repetidos = set(lista)
    return list(set_sin_repetidos)
    
    
def main():
    lista = int(input("Ingrese la cantidad de números a generar: "))
    print(guion(70))
    lista = cargar_lista(lista)
    print(F"Lista generada: {lista}")
    print(guion(70))
    print(F"¿Hay elementos repetidos? {hay_repetidos(lista)}")
    unicos = eliminar_repetidos(lista)
    print(guion(70))
    print(F"Lista sin repetidos: {unicos}")

if __name__ == "__main__":
    main()
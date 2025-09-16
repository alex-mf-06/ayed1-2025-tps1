import random as rd
#ejercicio 2 tp2
def guion(cantidad:int)-> str:
    """
    Devuelve una cadena de guiones del largo especificado por cantidad.
    """
    if cantidad < 1:
        raise ValueError("La cantidad debe ser un entero positivo.")
    return '-' * cantidad
def cargar_lista(cantidad:int)-> list[list[int]]:
    """
    Carga una lista de listas con números enteros aleatorios.

    """
    if cantidad < 1:
        raise ValueError("La cantidad debe ser un entero positivo.")
    lista = [rd.randint(1,100) for _ in range(cantidad)]
    return lista

def hay_repetidos(lista:list[int]) -> bool:
    """
    Verifica si hay elementos repetidos en la lista va a devolver True si hay repetidos y False si no.
    """
    for i in range(len(lista)):
        elem= lista[i]
        for elemento in lista[i+1:]:
            if elem == elemento:
                return True
    return False
def eliminar_repetidos(lista:list[int]) -> list[int]:
    """
    Elimina los elementos repetidos de la lista y devuelve una nueva lista sin duplicados.
    """
    lista_sin_repetidos = []
    for i in lista:
        if i not in lista_sin_repetidos:
            lista_sin_repetidos.append(i)
    return lista_sin_repetidos
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
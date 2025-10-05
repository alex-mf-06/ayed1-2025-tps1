import random
from typing import List
#ejercicio 1
def cargar_lista_aleatoria():
    """
    Carga una lista de números enteros aleatorios.

    """
    cantidad = random.randint(1, 9)  # Número aleatorio de dos dígitos
    lista = [random.randint(1000, 9999) for _ in range(cantidad)]
    return lista

def producto_lista(lista:List[int]) -> List[int]:
    """
    Calcula el producto de todos los elementos en la lista.

    """
    try: 
        if len(lista) == 0:
            raise ValueError("La lista está vacía.")
    except TypeError:
        print("Error: La entrada no es una lista válida.")
        return None
    producto = 1
    for i in lista:
        producto *= i
    return producto
def eliminar_elemento(lista:List[int], elemento:int) -> List[int]:
    """
    Elimina todos los valores de un elemento que pone el usuario en la lista.
    Si el elemento no está en la lista, devuelve la lista original.
    precondición: la lista no está vacía y debe ser una lista de enteros.
    postcondición: devuelve una lista sin el elemento que el usuario quiere eliminar.
    El elemento a eliminar debe ser un entero.

    """
    try:
        
        if len(lista) == 0 or not isinstance(elemento, int) :
            raise ValueError("La lista está vacía o el elemento a eliminar no es un entero.")
    except TypeError:
        print("Error: La entrada no es una lista válida.")
        return None
    
    return [i for i in lista if i != elemento] # esto elimina el elemento que el usuario quiere quitar
def es_capicua(lista:List[int]) -> bool:


    """
    Verifica si la lista es capicúa (se lee igual de izquierda a derecha que de derecha a izquierda).
    precondición: la lista no está vacía y debe ser una lista de enteros.
    postcondición: devuelve True si la lista es capicúa, False en caso contrario.

    """
    try:
        if len(lista) == 0:
            raise ValueError("La lista está vacía.")
    except TypeError:
        print("Error: La entrada no es una lista válida.")
        return None
    n = len(lista)
    
    for i in range(n//2):
        if lista[i] != lista[n-i-1]:
            return False
    return  False

guion = lambda x: "-" * x
lista = cargar_lista_aleatoria()
copia = lista[:]
producto = producto_lista(copia)
lista_cambiada = eliminar_elemento(copia, 756) #cambiar por un elemento que esté en la lista para ver que funciona
capicua = es_capicua(copia)
if __name__ == "__main__":
    print(guion(70))
    print(f"Lista generada: {lista}")
    print(guion(70))
    print(f"Producto de los elementos de la lista: {producto}")
    print(guion(70))
    print(f"Lista después de eliminar el elemento: {lista_cambiada}")
    print(guion(70))
    print(f"¿La lista es capicúa? {capicua}")
    print(guion(70))

#ejercicio 2


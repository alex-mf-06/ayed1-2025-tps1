import random
random.seed(42)  # Fijar la semilla para reproducibilidad
#ejercicio 1
def cargar_lista_aleatoria():
    """
    Carga una lista de números enteros aleatorios.

    """
    cantidad = random.randint(10, 99)  # Número aleatorio de dos dígitos
    lista = [random.randint(1000, 9999) for _ in range(cantidad)]
    return lista
def copiar_lista(lista):
    """
    Crea una copia de la lista proporcionada.

    """
    copia = []
    for i in lista:
        copia.append(i)
    return copia
def producto_lista(lista:list[int]) -> list[int]:
    """
    Calcula el producto de todos los elementos en la lista.

    """
    producto = 1
    for i in lista:
        producto *= i
    return producto
def eliminar_elemento(lista:list[int], elemento:int) -> list[int]:
    """
    Elimina todos los valores de un elemento que pone el usuario en la lista.

    """
    return [i for i in lista if i != elemento] # esto elimina el elemento que el usuario quiere quitar
def es_capicua(lista:list[int]) -> list[int]:


    """
    Verifica si la lista es capicúa (se lee igual de izquierda a derecha que de derecha a izquierda).

    """
    n = len(lista)
    copia = []
    for i in range(n//2):
        if lista[i] == lista[n-i-1]:
            copia.append(lista[i])
    return copia
guion = lambda x: "-" * x
lista = cargar_lista_aleatoria()
copia = copiar_lista(lista)
producto = producto_lista(copia)
lista_cambiada = eliminar_elemento(copia, 2824)
capicua = es_capicua(copia)
print(F"Lista original: {lista}")
print(F"Lista copiada: {copia}")
print(F"Producto de la lista copiada: {producto}")
print(F"Lista cambiada: {lista_cambiada}")
if len(capicua) > 0:
    print(F"Elementos comunes: {capicua}")
else:
    print("No hay elementos comunes.")

#ejercicio 2

def cargar_lista(cantidad:int)-> list[list[int]]:
    """
    Carga una lista de listas con números enteros aleatorios.

    """
    if cantidad < 1:
        raise ValueError("La cantidad debe ser un entero positivo.")
    lista = [random.randint(1,100) for _ in range(cantidad)]
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
#ejercicio 3 
def carg_lista():
    """
    cargar una lista con la cantidad  que se le solicita al usuario  
    """
    
    cantidad = int(input("Ingrese la cantidad de números a generar: "))
    lista = [i**2 for i in range(1,cantidad+1)]
    print(F"{lista}")
    print(f"Los ultimos 10 elementos son : {lista[-10:]}")
carg_lista()


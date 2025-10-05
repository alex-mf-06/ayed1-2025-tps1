
#ejercicio 4
guion = lambda x: "-" * x
def eliminar_valor_lista(lista: list[int], lista_eliminar: list[int]) -> list[int]:
    """
    Elimina todos los valores que se encuentran en lista_eliminar de la lista original.
    Si un valor de lista_eliminar no está en la lista original, se ignora.
    precondición: ambas listas no están vacías y deben ser listas de enteros.
    postcondición: devuelve la lista original sin los valores que se encuentran en lista_eliminar.
    """
    try:
        if len(lista) == 0 or len(lista_eliminar) == 0:
            raise ValueError("Ambas listas deben no estar vacías.")
    except TypeError:
        print("Error: La entrada no es una lista válida.")
        return None
    for i in lista_eliminar: # Itera sobre los elementos a eliminar
        while True:
            if i not in lista: # Si el elemento no está en la lista, sale del bucle
                break
            lista.remove(i)
    return lista # Lista final sin los valores eliminados
if __name__ == "__main__": 
    lista_a = [1,1,2,3,4,4,5,6,78,21]
    lista_con_valores_a_eliminar = [1, 4, 9, 20, 21]
    print(f"lista original : {lista_a}")
    print(guion(70))
    print(f"lista con valores a eliminar : {lista_con_valores_a_eliminar}")
    print(guion(70))
    print(f"lista final : {eliminar_valor_lista(lista_a, lista_con_valores_a_eliminar)}")
assert eliminar_valor_lista([1,2,3,4,5,6,7,8,9],[1,2,3]) == [4,5,6,7,8,9]
assert eliminar_valor_lista([1,2,3,4,5,6,7,8,9],[9]) == [1,2,3,4,5,6,7,8]
assert eliminar_valor_lista([], [1,2,3]) == None

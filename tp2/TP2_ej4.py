
#ejercicio 4
def guion(cantidad:int)-> str:
    """
    Devuelve una cadena de guiones del largo especificado por cantidad.
    """
    if cantidad < 1:
        raise ValueError("La cantidad debe ser un entero positivo.")
    return '-' * cantidad
def eliminar_valor_lista(lista: list[int], lista_eliminar: list[int]) -> list[int]:
    for i in lista_eliminar: # Itera sobre los elementos a eliminar
        while i in lista:    # Se repite hasta eliminar todas las ocurrencias
            lista.remove(i)
    return lista # Lista final sin los valores eliminados
lista_a = [1,1,2,3,4,4,5,6,78,21]
lista_con_valores_a_eliminar = [1, 4, 9, 20, 21]
print(f"lista original : {lista_a}")
print(guion(70))
print(f"lista con valores a eliminar : {lista_con_valores_a_eliminar}")
print(guion(70))
print(f"lista final : {eliminar_valor_lista(lista_a, lista_con_valores_a_eliminar)}")

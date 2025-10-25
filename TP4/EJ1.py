def es_capicua(cadena):
    """
    Esta función verifica si la palabra ingresada como parametro es capicúa.

    Pre:
        - Debe recibir solo str.

    Post:
        - Devuelve un boolean que si es capicua es True, y si no es capicua develve False.
    """

    lista = list(cadena)

    for i in range(len(lista)//2):
        if lista[i] != lista[-1 - i]:
            return False
    return True


assert es_capicua("reconocer") == True
assert es_capicua("ratón") == False

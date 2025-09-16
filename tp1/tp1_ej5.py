def es_oblongo(a:int)->bool:
    """
    Verifica si un número es oblongo.

    contrato: 
    - Precondiciones:
        * a (int) debe ser mayor o igual a 1.
    - Postcondiciones:
        * Devuelve True si a es un número oblongo, False en caso contrario.
        * Un número es oblongo si puede expresarse como el producto de dos enteros consecutivos.
        * Si a < 1 → devuelve False.
    """

    if a < 1:
        return False
    num = 1
    while num * (num + 1) <= a:
        if num * (num + 1) == a:
            return True
        num += 1
    return False
assert es_oblongo(6) == True
assert es_oblongo(8) == False
assert es_oblongo(12) == True
def es_triangular(num:int)->bool:
    """
    Verifica si un número es triangular.
    contrato:
    - Precondiciones:
        * num (int) debe ser mayor o igual a 1.
    - Postcondiciones:
        * Devuelve True si num es un número triangular, False en caso contrario.    
        * Un número es triangular si puede expresarse como la suma de los primeros n enteros positivos.
        * Si num < 1 → devuelve False.
    """
    if num < 1:
        return False
    n = 0
    triangular = 1
    while triangular < num:
        n += 1
        triangular = n * (n + 1) // 2
    return triangular == num
assert es_triangular(36) == True
assert es_triangular(8) == False
assert es_triangular(10) == True

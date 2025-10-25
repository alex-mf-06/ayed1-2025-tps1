def obtener_claves(clave: str) -> tuple:
    """
    Recibe una clave maestra de tipo string, de números enteros.

    Pre:
        - Debe recibir números enteros de tipo string.
        - No debe ser vacio

    Post:
        - Devuelve ambas claves en una tupla de 2 elementos que serian las claves obtenidas.
        - 1° Clave: Impar
        - 2° Clave: Par
    """

    return "".join(list(clave[::2])), "".join(list(clave[1::2]))


clave_maestra = "18293"
clave_impar, clave_par = obtener_claves(clave_maestra)


print(
    f"Clavesobtenidas de la clave maestra: {clave_maestra} \n- Clave 1: {clave_impar} \n- Clave 2: {clave_par}")
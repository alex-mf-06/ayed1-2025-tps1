# ejercicio 7 TP1 :

def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
    Args:
        anio (int): El año a evaluar.
    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dia_siguiente(dia:int, mes:int, anio:int)->tuple:
    if dia < 1 or mes < 1 or anio < 1:
        return (-1, -1, -1)
    dias_en_mes = [31, 28 + (1 if es_bisiesto(anio) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if dia > dias_en_mes[mes - 1]: # Verifica si el dia es valido para el mes y año dado
        return (-1, -1, -1)
    dia += 1
    if dia > dias_en_mes[mes - 1]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return (dia, mes, anio)
assert dia_siguiente(28, 2, 2020) == (29, 2, 2020) # Año bisiesto
assert dia_siguiente(28, 2, 2021) == (1, 3, 2021)  # Año no bisiesto
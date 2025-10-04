# ejercicio 2 TP1 :
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
    Args:
        anio (int): El año a evaluar.
    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    try:
        anio = int(anio)
    except ValueError:
        return False
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """Valida si una fecha es correcta.
    Args:
        dia (int): El día a validar.
        mes (int): El mes a validar.
        anio (int): El año a validar.
    precondiciones: dia, mes y anio deben ser enteros y no listas o tro tipo de argumentestos.
    postcondiciones:
    bool: True si la fecha es correcta, False en caso contrario.
    """
    try:
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)
    except ValueError:
        return False
    except TypeError:
        return False
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Lista de dias por mes
    if anio < 1: # Verifica si el año es valido
        return False
    if es_bisiesto(anio): # Si el año es bisiesto, febrero
        meses[1] = 29
    if mes > 0 and mes < 13: # Verifica si el mes es valido
        if dia > 0 and dia <= meses[mes - 1]: # Verifica si el dia es valido
            return True
    return False
print(validar_fecha(29, 2,[ 1,2,3,4])) # False
print(validar_fecha(29, 2, 2021)) # False
print(validar_fecha(31, 4, 2020)) # False


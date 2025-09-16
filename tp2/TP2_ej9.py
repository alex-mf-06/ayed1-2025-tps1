def multiplo_7_no_de_5(inicio:int , fin:int)-> list[int]:
    """
    Genera una lista de números que son múltiplos de 7 pero no de 5 en un rango dado
    """
    return [i for i in range(inicio, fin + 1) if i % 7 == 0 and i % 5 != 0]
print(multiplo_7_no_de_5(1, 100))
#ejercicio 10
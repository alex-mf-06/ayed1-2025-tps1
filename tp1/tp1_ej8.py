def dia_de_la_semana(dia:int, mes:int, anio:int)->int:
    """
    Calcula el día de la semana para una fecha dada usando la fórmula de Zeller.
    contrato:
    - Precondiciones:
        * dia (int) debe ser un día válido del mes.
        * mes (int) debe ser un mes válido (1-12).
        * anio (int) debe ser un año válido (mayor que 0).
        - Postcondiciones:
        * Devuelve un entero que representa el día de la semana (0=Domingo, 1=Lunes, ..., 6=Sábado).
        * Si la fecha es inválida → devuelve -1."""
    if mes < 3:
        mes += 12
        anio -= 1
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem
assert dia_de_la_semana(1, 1, 2022) == 6 # Sábado
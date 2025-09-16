# tp1_ej4.py
def calcular_cambio(precio:int, pago: int)-> list :
    """
    Calcula el cambio total de una compra en billetes de distintas denominaciones.
    contrato:
    - Precondiciones:
        * precio (int) debe ser mayor a 0.
        * pago (int) debe ser mayor o igual a precio.
    - Postcondiciones:
        * Devuelve una lista con la cantidad de billetes de cada denominación.
        * Si pago < precio → devuelve [-1].
    """
    billetes = [5000, 1000, 500, 200, 100, 50, 10] # Lista de billetes disponibles
    if pago < precio:
        return [-1] # Si el pago es menor que el precio, retorna [-1]
    cambio = pago - precio # Calcula el cambio a devolver
    total_billetes = [] # Lista para almacenar la cantidad de billetes de cada denominacion
    for billete in billetes: # Itera sobre cada billete disponible
        total_billetes.append(cambio // billete) # Calcula la cantidad de billetes de esa denominacion
        cambio %= billete # Actualiza el cambio restante
    return total_billetes # Retorna la lista de billetes

billetes = [5000, 1000, 500, 200, 100, 50, 10]
precio = 12730
pago = 20000
if pago < precio:
    print("El pago es menor que el precio.")
else:
    salida = calcular_cambio(precio, pago) # Llama a la funcion para calcular el cambio
    print(f"Cambio a devolver: ${pago - precio}")
    for i,s in enumerate(salida):
        if s:
            print(f"{s} billetes de ${billetes[i]}") # Imprime la cantidad de billetes de cada denominacion

from typing import List
# tp1_ej4.py

def calcular_cambio(precio:int, pago: int)-> List :
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
    try :
        precio = int(precio)
        pago = int(pago)
    except ValueError :
        print("Error: El precio y el pago deben ser números enteros.")
        return [-1]
    except TypeError :
        print("Error: El precio y el pago deben ser números enteros.")
        return [-1]
    
    billetes = [5000, 1000, 500, 200, 100, 50, 10] # Lista de billetes disponibles
    if pago < precio:
        return [-1] # Si el pago es menor que el precio, retorna [-1]
    cambio = pago - precio # Calcula el cambio a devolver
    total_billetes = [] # Lista para almacenar la cantidad de billetes de cada denominacion
    for billete in billetes: # Itera sobre cada billete disponible
        total_billetes.append(cambio // billete) # Calcula la cantidad de billetes de esa denominacion
        cambio %= billete # Actualiza el cambio restante
    print(cambio)
    return total_billetes # Retorna la lista de billetes

billetes = [5000, 1000, 500, 200, 100, 50, 10]
precio = "waza"
pago = "nana"
if __name__ == "__main__":
        salida = calcular_cambio(precio, pago) # Llama a la funcion para calcular el cambio
        if salida == [-1]:
            print("Error: El pago debe ser mayor o igual al precio.")
        else:
            print(f"Billetes de cada denominación para el cambio de {pago - precio} son:")
            for i in range(len(billetes)):
                print(f"{billetes[i]}: {salida[i]}")
def total_pago_viajes(cantidad:int) -> int:
    """
    Calcula el costo total de una cantidad de viajes aplicando descuentos por tramos.

    Contrato:
    - Precondiciones:
        * cantidad (int) debe ser mayor a 0.
    - Postcondiciones:
        * Devuelve el costo total como un entero.
        * Si cantidad <= 20 → sin descuento.
        * Si 20 < cantidad <= 30 → 20% descuento en los viajes adicionales.
        * Si 30 < cantidad <= 40 → 30% descuento en los viajes adicionales.
        * Si cantidad > 40 → 40% descuento en los viajes adicionales.
        * Si cantidad <= 0 → devuelve -1.
    """
     
    contador = 1
    precio = 1000
    total = 0
    if cantidad <= 0 :
        return -1
    for i in range(cantidad):
        if contador <= cantidad and contador <= 20 :
            contador += 1
            total += precio
        elif contador <= cantidad and contador <= 30 :
            contador += 1
            total +=  precio - precio * 0.2
        elif contador <= cantidad and contador <= 40 :
            contador += 1
            total += precio - precio * 0.3
        elif contador <= cantidad and contador > 40 :
            contador += 1
            total += precio - precio * 0.4
    return total
print(total_pago_viajes(22)) # Llama a la funcion para calcular el total a pagar por los viajes
print(total_pago_viajes(35)) # Llama a la funcion para calcular el total a pagar por los viajes
def carg_lista():
    """
    cargar una lista con la cantidad  que se le solicita al usuario  
    """
    
    try:
        cantidad = int(input("Ingrese la cantidad de números a generar: "))
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        return  # sale de la función si hay error

    # Si no hubo error, se ejecuta el resto del código:
    lista = [i**2 for i in range(1, cantidad + 1)]
    print(f"\nLista completa: {lista}")
    print(f"Los últimos 10 elementos son: {lista[-10:]}")
carg_lista()
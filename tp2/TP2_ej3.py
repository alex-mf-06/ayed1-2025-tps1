def carg_lista():
    """
    cargar una lista con la cantidad  que se le solicita al usuario  
    """
    
    cantidad = int(input("Ingrese la cantidad de números a generar: "))
    lista = [i**2 for i in range(1,cantidad+1)]
    print(F"{lista}")
    print(f"Los ultimos 10 elementos son : {lista[-10:]}")
carg_lista()
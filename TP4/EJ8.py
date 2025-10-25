def mostrar_ultm_subcadenas(cadena:str) -> str : 
    """
    Muestra las últimas 'n' subcadenas (palabras) de una cadena dada.
    La cantidad 'n' es solicitada al usuario dentro de la función.
    
    Precondiciones:
    - El parámetro 'cadena' debe ser un string.
    - El usuario debe ingresar un número entero positivo para la cantidad de subcadenas.
    - La cantidad ingresada no puede ser mayor al número total de palabras en la cadena.
    
    Postcondiciones:
    - Devuelve un nuevo string que contiene las últimas 'n' palabras de la cadena original,
      separadas por espacios.
    - Lanza TypeError si el parámetro 'cadena' no es un string.
    - Lanza ValueError si la cantidad ingresada por el usuario no es un número entero.
    """
    try:
        cadena = str(cadena)
        palabras = cadena.split()
        largo = len(palabras)

        while True:
            cantidad = int(input(f"Ingrese la cantidad de últimas palabras que desea ver (la cadena tiene {largo} palabras): \n"))
            if cantidad > 0 and cantidad <= largo:
                break
            print(f"Error: la cantidad debe ser un número entre 1 y {largo}.")

        ultimas_palabras = palabras[-cantidad:]
        return " ".join(ultimas_palabras)
    except TypeError:
        raise TypeError("El parámetro 'cadena' debe ser un string.")
    except ValueError:
        raise ValueError("La cantidad ingresada debe ser un número entero.")
    
frase_ejemplo = "La programación no solo consiste en escribir código que funcione, sino en crear soluciones claras, eficientes y fáciles de mantener, que otros puedan entender y mejorar con el tiempo"

resultado = mostrar_ultm_subcadenas(frase_ejemplo)
print(f"Las últimas subcadenas son: '{resultado}'")
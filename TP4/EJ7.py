
def eliminar_subcad_slizing(cadena:str) -> str:
    """
    
    La funcion se encarga de eliminar la cantida de cadenas que el usuario desee. 
    precondiciones : la cadena debe ser un string
    postcondiciones: devuelve la cadena sin la cantidad de elementos que el usuario desee.

    """
    try : 
        cadena = str(cadena)
        cadena = cadena.split()
        largo = len(cadena)
        while True : 
            cantidad = int(input(f"Ingrese la cantidad de palabras desea que se borren sabiendo que (la cadena tiene {largo} palabras) :  \n"))
            if cantidad > 0 and cantidad <= largo :
                break
            elif cantidad > largo or cantidad < 0 :
                print(f"Error la cantidad no puede ser mayor o menor a 0 \n")
        return " ".join(cadena[:- cantidad])

    except TypeError:
        raise TypeError("la cadena debe ser un str")
    except ValueError:
        raise ValueError("la cantidad debe ser un numero entero")
    

def eliminar_subcad_for(cadena:str) -> str:
    """
    Elimina una cantidad de palabras del final de la cadena, según lo especificado por el usuario, usando un bucle.
    
    Precondiciones:
    - La cadena debe ser un string.
    - El usuario debe ingresar un número entero para la cantidad de palabras a eliminar.

    Postcondiciones:
    - Devuelve la cadena sin la cantidad de palabras finales que el usuario especificó.
    - Lanza TypeError si la cadena no es un string.
    - Lanza ValueError si la cantidad ingresada no es un número entero.
    """
    try:
        cadena = str(cadena)
        palabras = cadena.split()
        largo = len(palabras)
        
        while True:
            cantidad = int(input(f"Ingrese la cantidad de palabras que desea borrar (la cadena tiene {largo} palabras): \n"))
            if 0 < cantidad <= largo:
                break
            print(f"Error: la cantidad debe ser un número entre 1 y {largo}.")
        
        palabras_a_mantener = largo - cantidad
        nueva_cadena_lista = [ palabras[i] for i in range(palabras_a_mantener)]   
        return " ".join(nueva_cadena_lista)
    except TypeError:
        raise TypeError("La cadena debe ser un str.")
    except ValueError:
        raise ValueError("La cantidad debe ser un número entero.")

cadena = "La programación no solo consiste en escribir código que funcione, sino en crear soluciones claras, eficientes y fáciles de mantener, que otros puedan entender y mejorar con el tiempo"

print(f"Con slizing : {eliminar_subcad_slizing(cadena)}\n")
print(f"Con for : {eliminar_subcad_for(cadena)}")

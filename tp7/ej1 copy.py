

def cant_digitos(numero:int) -> int:

    """
    
    Esta funcion se encarga de que el usuario que va ingresar un numero a la funcion 
    para luego retorne un entero que representa la cantidad de de digitos que tiene el numero por ejemplo numero = 100 la cantidad de digitos que debe retornar es 3 .
    precondiciones : el elemento que le ingresen debe ser un numero entero y no decimal 
    postcondiciones : retorna un numero entero que representan la cantidad de digitos que tiene el numero ingresado. va a retornar 0 si el parametro que se ingreso no es un numero 

    
    """
    try :
        if numero == int(numero) : 
            numero = abs(numero)
            if numero < 10:
                return 1
            else :
                return 1 + cant_digitos(numero // 10)

        else :
            return 0
    except TypeError:
        return 0
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    m = cant_digitos(12456)
    print(m)
    assert cant_digitos(100) == 3
    assert cant_digitos(2448) == 4
    assert cant_digitos(0) == 1
    assert cant_digitos(-123) == 3
def validar_n_entero_y_posittivo(numero_str:str)->int|None:
    """Solicita al usuario ingresar un número entero no negativo y valida la entrada.
    precondiciones: debe ser un string que represente un número entero.
    postcondiciones:
    - Si la entrada es válida, la función retorna None.
    - Si la entrada no es un número entero o es negativa, se lanza una excepción ValueError con un mensaje adecuado.
    """

    try : 
        
        numero = int(numero_str)
        if numero < 0:
            print("El número debe ser no negativo.")
            return None
        else:
            print("La entrada es válida.")
            return numero
    except ValueError:
        print("La entrada debe ser un número entero válido.")
        return None

if __name__ == "__main__":
    assert validar_n_entero_y_posittivo("2342") == 2342
    assert validar_n_entero_y_posittivo("-5") == None
    assert validar_n_entero_y_posittivo("abc") == None
    assert validar_n_entero_y_posittivo("123") == 123

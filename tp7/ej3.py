
def suma_recursiva(numero : int) -> int:
    """

    Esta funcion se encarga el numero que ingrese el usuario se va a seguir sumando consecutivamente . 
    si el numero es 10 la suma va hacer 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 55
    precondiciones : El valor que le va  a pdsar debe ser un entero y debe ser positivo 
    potcondiciones: devuelve un entero que es la suma del numero que puso el usuario y los anteriores numeros que estan anteriores a ese numero .


    """
    try :
        if numero == int(numero) and numero > 0: 
            numero = abs(numero)
            if numero == 1 :
                return numero
            else :
                return numero + suma_recursiva(numero - 1)
        else :
            return 0
    except TypeError:
        return 0
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    print(suma_recursiva(10))
    assert suma_recursiva(10) == 55
    assert suma_recursiva(0) == 0
    assert suma_recursiva(-123) == 0
    assert suma_recursiva(1) == 1
    assert suma_recursiva(2) == 3
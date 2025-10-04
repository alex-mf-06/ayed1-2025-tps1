#ejeercicio 6 TP1 :
def concatenar_numeros(a:int, b:int)->int:
    """
    Concatena dos números enteros.
    contrato:
    - Precondiciones:
        * a (int) debe ser mayor o igual a 0.
        * b (int) debe ser mayor o igual a 0.
    - Postcondiciones:
        * Devuelve un entero que representa la concatenación de a y b.
    """
    try :
        a = int(a)
        b = int(b)
    except ValueError :
        print("Error: Ambos números deben ser enteros.")
        return -1
    except TypeError :
        print("Error: Ambos números deben ser enteros.")
        return -1
    dig = 0
    aux = b
    while True:
        if aux > 0:
           dig += 1
           aux //= 10
        else:
           break
    a = a * (10 ** dig) 
    return a + b
assert concatenar_numeros(12, 34) == 1234
assert concatenar_numeros(5, 678) == 5678
assert concatenar_numeros("n", 34) == -1
assert concatenar_numeros(12, "m") == -1